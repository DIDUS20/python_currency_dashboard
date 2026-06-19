
import requests
from domain.repositories import CurrencyRepository, CurrencyRepositoryError


class CurrencyRepo(CurrencyRepository):
    def __init__(self, host: str | None, key: str | None, def_list_cur = {}, base_currency = ""):
        self.data: dict[str, float] = {}
        self.api_host = host
        self.api_key = key
        
        self.base_cur = base_currency
        self.list_cur = def_list_cur

    def get_currencies_list(self):
        if not self.api_host or not self.api_key:
            raise CurrencyRepositoryError("Brak konfiguracji API")
             
        url = f"{self.api_host}/{self.api_key}/latest/{self.base_cur}"
        
        print(url)

        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except ValueError:
            raise ValueError("Problem z danymi")
        except ConnectionError:
            raise CurrencyRepositoryError("Problem z połączeniem")
        except Exception:
            raise CurrencyRepositoryError("Problem z repo")
        
        
        all_rates = data.get("conversion_rates", {})
        self.data = {cur: all_rates[cur] for cur in self.list_cur if cur in all_rates}
        return self.data
    
    def change_base_currency(self, new_base_cur : str):
        self.base_cur = new_base_cur
        
    def get_base_currency(self): return self.base_cur
    
    def get_list(self): return self.list_cur

    
    