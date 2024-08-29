from Milkshake import Milkshake
class MilkshakeDecorator(Milkshake):
    def __init__(self,ms:Milkshake):
        self.__milkshake__ = ms

    def preco(self) -> float:
        return self.__milkshake__.preco()
    
class Morango(MilkshakeDecorator):
    def preco(self) -> float:
        return super().preco() + 2

class DoceDeLeite(MilkshakeDecorator):
    def preco(self) -> float:
        return super().preco() + 4
    
class Amendoim(MilkshakeDecorator):
    def preco(self) -> float:
        return super().preco() + 3
    
class GotasDeChocolate(MilkshakeDecorator):
    def preco(self) -> float:
        return super().preco() + 6