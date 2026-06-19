from abc import ABC, abstractmethod

class CurrencyRepository(ABC):

    @abstractmethod
    def get_currencies_list(self): 
        pass
    
    @abstractmethod
    def change_base_currency(self, new_base_cur : str):
        pass
    
    @abstractmethod
    def get_base_currency(self) -> str:
        pass
    
    @abstractmethod
    def get_list(self) -> list[str]:
        pass
    
class CurrencyRepositoryError(Exception):
    "Błąd podczas pobierania danych z repozytorium walut"
    pass