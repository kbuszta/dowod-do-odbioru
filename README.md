# dowod-do-odbioru
Ten kod realizuje automatyczne sprawdzanie statusu wniosku o dowód osobisty poprzez stronę internetową Ministerstwa Sprawiedliwości. Głównym celem jest monitorowanie, czy wniosek jest już gotowy do odebrania, a w przypadku tego zdarzenia, wysłanie powiadomienia e-mailem.

## Przed uruchomieniem
1. Zaimportuj niezbędne zasoby. Wykorzystane moduły to `json`, `os`, `sys`, `smtplib` oraz różne klasy z modułów `email.message`, `bs4` (BeautifulSoup) i `selenium`.
2. Upewnij się, że plik config.json znajduje się w tym samym folderze, co plik main.py. Skrypt pobiera ścieżkę folderu, w którym się znajduje, aby później odnosić się do pliku konfiguracyjnego znajdującego się w tym samym folderze. 
3. Zaktualizuj plik config.json. Jako adres mailowy nadawcy najlepiej sprawdził się w moim przypadku adres ze strony outlook.com, dlatego w pliku config.json pozostawiłem konfigurację SMTP dla tego właśnie adresu.
4. (Opcjonalnie) Zaktualizuj ścieżki w pliku .bat. (Więcej informacji w części dotyczącej automatycznego uruchamiania skryptu). 

## Automatyczne uruchamianie skryptu sprawdzającego po uruchomieniu komputera z systemem Windows

Istnieje możliwość automatycznego uruchamiania skryptu przy każdym włączeniu komputera. 

* Jedną z propozycji realizujących to zadanie może być utworzenie pliku .bat, który uruchamia niniejszy skrypt ORAZ umieszczenie go (pliku .bat) w folderze "Autostart". 
* Dopóki plik .bat będzie obecny w folderze "Autostart", dopóty będzie sprawdzać status dowodu przy każdym uruchomieniu, dlatego należy pamiętać o usunięciu tego pliku po otrzymaniu informacji o dowodzie osobistym gotowym do odbioru.
* Przykładowe ścieżki:
  
ŚCIEŻKA_DO_SKRYPTU_AKTYWUJĄCEGO_WIRTUALNE_ŚRODOWISKO_PYTHON -> C:\Users\Michal\PycharmProjects\SprawdzStatusDowodu\venv\Scripts\activate

ŚCIEŻKA_DO_PLIKU_MAIN.PY -> C:\Users\Michal\PycharmProjects\SprawdzStatusDowodu\main.py


## Pozostałe informacje
* Uruchomiony skrypt działa w tle - nie wyświetla okna przeglądarki dzięki atrybutowi "headless".
* Zastanawiałem się, czy nie umieścić hasła do poczty np. w menedżerze poświadczeń, ale mając na uwadze prostotę skryptu zdecydowałem się pozostać przy tekstowym pliku konfiguracyjnym.
