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
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return self.message