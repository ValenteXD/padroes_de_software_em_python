from Viagens import Viagens
from ReservaCarro import ReservaCarro
from ReservaVoo import ReservaVoo

class Fachada:
    def __pagar__():
        if Viagens.pagamento("Insira seu método de pagamento: "):
            print("pagamento aprovado!")

    def destinos():
        destinos = Viagens.verDestinos()
        i=1
        for cidade in destinos:
            print(i,"- ",cidade)
            i+=1
        print(i,"- para voltar ao menu inicial")
        while True:
            entrada = input("Digite o número do destino que gostaria de ver ofertas: ")
            try:
                entrada = int(entrada)
                if entrada == i:
                    return
                elif entrada>i or entrada<1:
                    raise Exception()
                break
            except:
                print("ERRO! Isto não é um número válido")
        
        hoteis = Viagens.verHoteis(destinos[entrada-1])
        cidade = destinos[entrada-1]
        i=1
        for hotel in hoteis:
            print(i,hotel.nome," quartos disponíveis: ",hotel.vagas," valor: ",hotel.custo)
            i+=1
        print(i,"- para voltar ao menu inicial")
        while True:
            entrada = input("digite o número do hotel que gostaria de reservar: ")
            try:
                entrada = int(entrada)
                if entrada == i:
                    return
                elif entrada>i or entrada<1:
                    raise Exception()
                break
            except:
                print("ERRO! Isto não é um número válido")
        selecionado=hoteis[entrada-1]
        
        if selecionado.vagas<=0:
            print("Desculpe não há quartos disponíveis para este hotel")
            return
        
        while True:
            entrada = input("quantos dias gostaria de passar conosco em ",selecionado.nome,"? ")
            try:
                entrada = int(entrada)
                if entrada<1:
                    raise Exception()
                break
            except:
                print("ERRO! Isto não é um número válido")
        
        valorCarro = ReservaCarro.reserva(cidade, entrada)
        valorVoo = ReservaVoo.reserva(cidade)
        custo = selecionado.custo * entrada + valorVoo + valorCarro 
        print("Obrigado por selecionar ",selecionado.nome," o valor total é ",custo," reais")
        Fachada.__pagar__()
        selecionado.vagas-=1