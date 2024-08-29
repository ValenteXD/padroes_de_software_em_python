from Pedido import Pedido
class PedidoPronto(Pedido):
    def proximoEstado(self) -> str:
        return  "saiu para entrega"

    def verificaEstado(self) -> None:
        print("Seu pedido já está pronto")