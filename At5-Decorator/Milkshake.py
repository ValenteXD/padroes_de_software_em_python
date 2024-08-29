from abc import ABC, abstractmethod

class Milkshake(ABC):
    @abstractmethod
    def preco(self):
        pass

class VanillaMilkshake(Milkshake):
    def preco(self)->float:
        return 5
    
class ChocolateMilkshake(Milkshake):
    def preco(self)->float:
        return 6