from abc import ABC, abstractmethod
class PlayerCharacter(ABC):
    @abstractmethod
    def atk():
        pass
    
    @abstractmethod
    def defend():
        pass
