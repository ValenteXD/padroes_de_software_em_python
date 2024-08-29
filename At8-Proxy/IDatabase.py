from abc import ABC, abstractmethod

class IDatabase(ABC):
    @abstractmethod
    def requestAccess(self, id:str, data:str) ->str:
        pass
    
    @abstractmethod
    def __init__(self, data) -> None:
        pass