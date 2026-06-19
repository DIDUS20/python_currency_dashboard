# Python Currency Dashboard

A simple desktop application for tracking selected currency exchange rates and compare currencies.


## Wymagania
- Python 3.10+ (zalecany)
- `requests`
- `customtkinter`

## Instalacja

1. Sklonuj repozytorium lub skopiuj pliki do katalogu projektu.
2. Skonfiguruj config.json.
3. Utwórz i aktywuj wirtualne środowisko:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
4. Zainstaluj zależności:
```powershell
python -m pip install requests customtkinter
```

## Uruchomienie
W katalogu projektu uruchom:
```powershell
python main.py
```

## Struktura projektu
- `main.py` — punkt startowy aplikacji
- `presentation/window.py` — interfejs graficzny
- `data/currency_freaks_repo.py` — pobieranie kursów walut
- `domain/repositories.py` — interface repozytorium danych

## Użycie
- Kliknij `Load`, aby pobrać najnowsze kursy lub zmienić walutę bazową.
- Zobacz tabelę kursów walut.
- Skorzystaj z konwertera, aby przeliczyć kwotę między walutami.

## Uwagi
- W przypadku problemów z siecią wyświetlany jest komunikat błędu.


