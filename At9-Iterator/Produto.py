class Produto:
    def __init__(self,nome:str,preco:float,categoria:str) -> None:
        self.__maxNome: int = 25
        self.__maxNomeCategoria: int = 10
        self.nome = nome[:self.__maxNome]
        self.__preco = preco
        self.__categoria = categoria[:self.__maxNomeCategoria]

    def isCategoria(self,categoria:str) -> bool:
        return categoria == self.__categoria
    
    def toStr(self) -> str:
        return self.__categoria +" "*(self.__maxNomeCategoria-len(self.__categoria))+": "+ self.nome+" "+"-"*(self.__maxNome-len(self.nome)+1)+" R$"+f"{self.__preco:.2f}"
    
    def getPreco(self) -> float:
        return self.__preco