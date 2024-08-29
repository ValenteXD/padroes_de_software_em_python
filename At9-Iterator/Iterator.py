from Produto import Produto
class Iterator:
    def __init__(self, lista:list[Produto], categorias:list[str]) -> None:
        self.__lista = lista
        self.__index:int = 0
        self.__categorias = categorias
        self.__categoriaAtual: int = 0
        self.__subLista = []

    def __filtro(self) -> list[Produto]:
        novaLista:list[Produto] = []
        for p in self.__lista:
            if p.isCategoria(self.__categorias[self.__categoriaAtual]):
                novaLista.append(p)
        self.__categoriaAtual+=1
        novaLista.sort(key=Produto.getPreco)
        return novaLista

    def proximo(self) -> Produto:
        if self.__index >= len(self.__lista):
            return
        if len(self.__subLista) == 0:
            self.__subLista = self.__filtro()
        value = self.__subLista[0]
        self.__subLista.remove(value)
        self.__index+=1
        return value
    
    def restantes(self) -> int:
        return len(self.__lista) - self.__index
    
    def getIndice(self) -> int:
        return self.__index