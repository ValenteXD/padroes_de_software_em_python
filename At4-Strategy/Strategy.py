from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def exec():
        pass