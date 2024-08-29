from Milkshake import VanillaMilkshake, ChocolateMilkshake
from MilkshakeDecorator import Morango, DoceDeLeite, GotasDeChocolate, Amendoim

if __name__=="__main__":
    menu = {
        1:VanillaMilkshake,
        2:ChocolateMilkshake,
    }
    decorators = {
        1:Morango,
        2:DoceDeLeite,
        3:Amendoim,
        4:GotasDeChocolate,
    }
    while True:
        entrada = input("Qual tipo de milkshake vc gostaria?\n1: Baunilha\n2: Chocolate\n")
        try:
            sabor = int(entrada)
            if sabor!=1 and sabor!=2:
                raise Exception()
            meuDelicioso = menu[sabor]()
            break
        except:
            print("Erro! Entrada inválida")
    while True:
        entrada = input("Gostaria de adicionar algo no seu Milkshake?\n1: Morangos\n2: Doce de Leite\n3: Amendoim\n4: Gotas de Chocolate\n5: Finalizar\n")
        try:
            adicional = int(entrada)
            if adicional<1 and adicional>5:
                raise Exception()
            elif adicional == 5:
                break
            meuDelicioso = decorators[adicional](meuDelicioso)
        except:
            print("Erro! Entrada inválida")
    print("O valor final do seu milk shake é R$",meuDelicioso.preco())