from Pedido import Pedido
class PedidoProcessando(Pedido):
    def proximoEstado(self) -> str:
        return "em preparo"

    def verificaEstado(self) -> None:
        print("Por favor aguarde enquanto confirmamos seu pedido com o restaurante")