from Pedido import Pedido
class PedidoPreparando(Pedido):
    def proximoEstado(self) -> str:
        return  "pronto para entrega"

    def verificaEstado(self) -> None:
        print("seu pedido está sendo preparado")