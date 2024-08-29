from PedidoProcessando import PedidoProcessando
from PedidoPreparando import PedidoPreparando
from PedidoPronto import PedidoPronto
from PedidoEmTransito import PedidoEmTransito
from PedidoEntregue import PedidoEntregue

class CentralDePedidos:
    __states__ = {
        "aguardando confirmação do restaurante": PedidoProcessando(),
        "em preparo": PedidoPreparando(),
        "pronto para entrega": PedidoPronto(),
        "saiu para entrega": PedidoEmTransito(),
        "entregue": PedidoEntregue(),
    }
    def __init__(self) -> None:
        self.__currState__ = "aguardando confirmação do restaurante"
        print("Seu pedido foi realizado com sucesso! Aguarde para confirmarmos com o restaurante")

    def __getStatus__(self) -> None:
        self.__states__[self.__currState__].verificaEstado()
            
    def __stateTrasitions__(self) -> None:
        self.__currState__ = self.__states__[self.__currState__].proximoEstado()
            
    def updateStatus(self):
        self.__stateTrasitions__()
        self.__getStatus__()

    def checkStatus(self):
        self.__getStatus__()