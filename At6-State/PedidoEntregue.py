from Pedido import Pedido
class PedidoEntregue(Pedido):
    def proximoEstado(self) -> str:
        print("Obrigado por comprar conosco, aproveite seu pedido")
        return "entregue"

    def verificaEstado(self) -> None:
        print("Seu pedido foi entregue")