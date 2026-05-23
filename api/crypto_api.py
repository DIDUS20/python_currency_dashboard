import requests


def get_crypto_prices():
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin,ethereum,solana,dogecoin"
        "&vs_currencies=pln"
        "&include_24hr_change=true"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "BTC": {
                "price": data["bitcoin"]["pln"],
                "change": round(data["bitcoin"]["pln_24h_change"], 2)
            },
            "ETH": {
                "price": data["ethereum"]["pln"],
                "change": round(data["ethereum"]["pln_24h_change"], 2)
            },
            "SOL": {
                "price": data["solana"]["pln"],
                "change": round(data["solana"]["pln_24h_change"], 2)
            },
            "DOGE": {
                "price": data["dogecoin"]["pln"],
                "change": round(data["dogecoin"]["pln_24h_change"], 2)
            }
        }

    except requests.RequestException as e:
        print("Crypto API Error:", e)
        return {}
    except (ValueError, KeyError) as e:
        print("Crypto API Parsing Error:", e)
        return {}