from Armazem import Armazem
from Iterator import Iterator
from Produto import Produto
if __name__=="__main__":
    estoque = Armazem([
        Produto("RTX 4060",1999.99,"Hardware"),
        Produto("Elden Ring",350.00,"Videogames"),
        Produto("RX6600",1299.90,"Hardware"),
        Produto("PS5 com leitor de disco",5499.99,"Console"),
        Produto("Super Mario Bros. Wonder",299.99,"Videogames"),
        Produto("Persona 5 Royal",249.90,"Videogames"),
    ])
    iterator = Iterator(estoque.getProdutos(),["Videogames","Console","Hardware"])
    while iterator.restantes()>0:
        print(iterator.proximo().toStr())