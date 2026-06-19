# Python Currency Dashboard

A simple desktop application for tracking selected currency exchange rates and cryptocurrency prices in PLN.

## Features

- Pobieranie kursów walut z API NBP
- Pobieranie cen kryptowalut (Bitcoin, Ethereum, Solana, Dogecoin) z CoinGecko
- Wyświetlanie danych w interfejsie graficznym z CustomTkinter
- Konwerter walut między PLN, USD, EUR, GBP i CHF
- Przycisk odświeżania danych w czasie rzeczywistym

## Wymagania

- Python 3.10+ (zalecany)
- `requests`
- `customtkinter`
- `matplotlib` (jeśli projekt będzie rozszerzany o wykresy)
- `pillow` (opcjonalnie dla grafiki)

## Instalacja

1. Sklonuj repozytorium lub skopiuj pliki do katalogu projektu.
2. Utwórz i aktywuj wirtualne środowisko:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Zainstaluj zależności:

```powershell
python -m pip install requests customtkinter matplotlib pillow
```

## Uruchomienie

W katalogu projektu uruchom:

```powershell
python main.py
```

## Struktura projektu

- `main.py` — punkt startowy aplikacji
- `gui/app.py` — logika i interfejs graficzny
- `api/currency_api.py` — pobieranie kursów walut z NBP
- `api/crypto_api.py` — pobieranie cen kryptowalut z CoinGecko
- `utils/` — pomocnicze narzędzia i moduły
- `assets/` — zasoby graficzne lub multimedialne (opcjonalnie)

## Użycie

- Kliknij `Aktualizuj dane`, aby pobrać najnowsze kursy.
- Zobacz tabelę kursów walut oraz ceny kryptowalut.
- Skorzystaj z konwertera, aby przeliczyć kwotę między walutami.

## Uwagi

- Aplikacja obsługuje tylko wybrane waluty: `PLN`, `USD`, `EUR`, `GBP`, `CHF`.
- W przypadku problemów z siecią wyświetlany jest komunikat błędu.
- Możesz rozbudować projekt o wykresy historyczne lub dodatkowe kryptowaluty.

## Licencja

Projekt nie zawiera przypisanej licencji w tym repozytorium.

