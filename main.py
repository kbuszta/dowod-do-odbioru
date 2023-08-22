import json
import os
import sys
import smtplib
from email.message import EmailMessage
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Pobranie ścieżki do folderu zawierającego aktualnie uruchamiany skrypt
script_folder = os.path.dirname(os.path.abspath(sys.argv[0]))

# Odczyt konfiguracji z pliku JSON
config_file_path = os.path.join(script_folder, "config.json")
with open(config_file_path, "r") as json_file:
    config = json.load(json_file)

def initialize_driver():
    # Inicjalizacja przeglądarki w trybie headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(chrome_options)

def check_status(driver, numer_wniosku):
    # Otwarcie strony i sprawdzenie statusu wniosku
    driver.get("https://moj.gov.pl/uslugi/engine/ng/index?xFormsAppName=SprawdzCzyDowodJestGotowy&xFormsOrigin=EXTERNAL")
    numer_wniosku_input = driver.find_element(By.ID, "NumerWniosku")
    numer_wniosku_input.send_keys(numer_wniosku)
    sprawdz_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sprawdź')]")
    sprawdz_button.click()
    status_list_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "status-list")))
    return status_list_element.get_attribute("outerHTML")

def send_email(subject, content):
    # Tworzenie wiadomości e-mail i wysłanie
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = config["adres_email_nadawcy"]
    msg['To'] = config["adres_email_odbiorcy"]
    with smtplib.SMTP(config["smtp_adres"], config["port_smtp"], timeout=120) as server:
        server.starttls()
        server.login(config["adres_email_nadawcy"], config["haslo_nadawcy"])
        server.send_message(msg)

try:
    # Inicjalizacja przeglądarki
    driver = initialize_driver()

    # Sprawdzenie statusu wniosku
    status_list_html = check_status(driver, config["numer_wniosku"])
    soup = BeautifulSoup(status_list_html, "html.parser")
    completed_li = soup.find_all("li", class_=lambda x: x and "completed" in x)[-1]

    # Jeśli wniosek jest gotowy, wyślij e-mail
    if "Dowód gotowy do odebrania" in completed_li.get_text():
        send_email("Dowód gotowy do odebrania", ":)")

finally:
    # Zamknięcie przeglądarki po zakończeniu
    driver.quit()