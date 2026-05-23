import requests


def get_currency_rates():
    url = "https://api.nbp.pl/api/exchangerates/tables/A?format=json"
    supported_codes = {"USD", "EUR", "GBP", "CHF"}

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        rates = data[0].get("rates", [])
        selected = {
            rate["code"]: rate["mid"]
            for rate in rates
            if rate.get("code") in supported_codes
        }

        return selected

    except requests.RequestException as e:
        print("Currency API Error:", e)
        return {}
    except (ValueError, KeyError, IndexError) as e:
        print("Currency API Parsing Error:", e)
        return {}