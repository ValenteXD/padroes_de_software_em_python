from Pedido import Pedido
class PedidoEmTransito(Pedido):
    def proximoEstado(self) -> str:
        return "entregue"

    def verificaEstado(self) -> None:
        print("Aguenta firme que nosso entregador já está a caminho")