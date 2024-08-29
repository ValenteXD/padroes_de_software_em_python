import time
class ReservaCarro:
    __tabelaPreco__={
        "Orlando":300,
        "Acapulco":200,
        "Natal":80,
    }
    def reserva(local,dias):
        print("buscando melhor valor de carros para aluguel na região...")
        time.sleep(3)
        return ReservaCarro.__tabelaPreco__[local]*dias
