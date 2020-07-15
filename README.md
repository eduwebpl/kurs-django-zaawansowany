# Kurs Python i Django - Techniki Zaawansowane

To repozytorium zawiera kod źródłowy do kursu [Python i Django - Techniki Zaawansowane](https://eduweb.pl/programowanie-i-www/python/python-i-django-techniki-zaawansowane) dostępnego w serwisie [eduweb.pl](https://eduweb.pl).

### Pobranie repozytorium

Aby korzystać z plików źródłowych do tego kursu, utwórz w dogodnym dla Ciebie miejscu w swoim systemie nowy katalog, np. **kurs**.

Przejdź do tego katalogu używając terminala i wpisz `git clone https://github.com/eduwebpl/kurs-django-zaawansowany.git`. Adres repozytorium skopiujesz klikając powyżej przycisk **Clone or download**.

Jeśli nie czujesz się jeszcze swodobnie w pracy z terminalem (wierszem poleceń), skorzystaj z naszych darmowych poradników na ten temat:

- [Podstawy pracy z Terminalem - macOS / Linux](https://www.youtube.com/watch?v=fAuDnN3C64o)
- [Podstawy pracy z Wierszem poleceń - Windows](https://www.youtube.com/watch?v=gohuR6-wT0Y)

### Podział plików źródłowych

Dzięki podzieleniu repozytorium na wiele gałęzi, masz dostęp do dwóch wersji plików źródłowych do każdej lekcji: startowych i końcowych. Dzięki temu możesz podczas oglądania kursu pracować razem z autorem na dokładnie takich samych plikach startowych, a gdy chcesz podejrzeć wersję plików z końca danej lekcji, również masz taką możliwość.

Katalogi z plikami źródłowymi, a co za tym idzie również gałęzie repozytorium, numerowane są od **01**. Oglądając lekcję, od razu zauważysz jaki katalog autor otworzył w swoim edytorze. Widząc **01**, wpisz w swoim terminalu `git checkout 01`, a w katalogu głównym pojawią się właśnie te pliki. Do wersji plików z końca danej lekcji, przejdziesz wpisując `git checkout 01-finish`. Dokładnie tak samo będzie w kolejnych lekcjach, np. `git checkout 13` i `git checkout 13-finish`.

Zdarzają się jednak przypadki, gdy prezentowany przykład (np. większa aplikacja) rozłożony jest na kilka lekcji. Jeśli zatem zobaczysz, że autor ma w swoim edytorze otwarty np. katalog **14**, wpisz `git checkout 14` i pracuj razem z nim. Jeśli w kolejnej lekcji nadal widzisz w edytorze autora ten sam katalog, oznacza to, że nadal pracujemy na tych samych plikach źródłowych. Możesz po prostu kontyuuować pracę razem z autorem. Jeśli jednak chciałbyś dostać się do plików startowych dla tej lekcji, wpisz `git checkout 14.2` (pliki startowe w tym przypadku będą identyczne jak pliki końcowe z commita **14-finish**). Wersję końcową dla tej lekcji podejrzysz wpisując `git checkout 14.2-finish`. Jeśli w kolejnej lekcji autor przeskoczy do katalogu **15**, oznacza to, że podzielony przykład już się zakończył i przechodzicie to nowego przykładu. Zrobisz to wpisując `git checkout 15`.

### Uruchomienie projektu
1. Przejdź do katalogu z kodem (nazwany jest on tak jak branch, zgodnie z numerem lekcji)
1. Zainstaluj zależności komendą
    ```
    pip install -r requirements_develop.txt
    ```
1. Jeżeli w katalogu z lekcją nie ma pliku .env możesz go utworzyć z pliku sample.env.
    ```
   cp sample.env .env
    ```
1. Wgraj migracje
    ```
    python manage.py migrate
    ```
   
   Ważna informacja: Podczas wykonywania migracji przy przechodzeniu z lekcji na lekcję mogą wystąpić błedy. Usuń wtedy istniejącą bazę i utwórz nową.
   Baza domyślnie tworzy się w katalogu z manage.py i jest pod nazwą db.sqlite3
   
1. Uruchom serwer deweloperski
    ```
    python manage.py runserver
    ```
1. Opcjonalnie możesz uruchomić przeglądarkę z adresem [http://127.0.0.1:8000]([http://127.0.0.1:8000])


### Wersja ZIP

Git to potężne narzędzie, które powinien znać każdy programista. Jeśli jednak jeszcze nie czujesz się z nim swobodnie lub wolisz mieć dostęp do wszystkich plików źródłowych na raz, możesz pobrać je w formie paczki ZIP na [stronie kursu](https://eduweb.pl/kursy/javascript/javascript-podstawy.html).

Jeśli natomiast chcesz nauczyć się korzystania z systemu kontroli wersji Git, polecamy nasz obszerny materiał na ten temat: [Kurs Git System Kontrol Wersji](https://eduweb.pl/kursy/javascript/git-system-kontroli-wersji.html).

### Miłego odbioru!

Pozostało Ci już tylko rozpocząć naukę. Miłego odbioru!

PS. Jeśli napotkasz jakieś trudności z korzystaniem z plików źródłowych, [skontaktuj się z nami](https://eduweb.pl/kontakt/), pomożemy!
