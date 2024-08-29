import time
class ReservaVoo:
    __tabelaPreco__={
        "Orlando":8000,
        "Acapulco":5000,
        "Natal":1000,
    }
    def reserva(local):
        print("buscando voôs disponíveis...")
        time.sleep(3)
        return ReservaVoo.__tabelaPreco__[local]
