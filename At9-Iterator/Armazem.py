from Produto import Produto
class Armazem:
    def __init__(self, items:list[Produto]) -> None:
        self.__items = items

    def getProdutos(self) -> list[Produto]:
        return self.__items