from abc import ABC, abstractmethod

class Pedido(ABC):
    @abstractmethod
    def proximoEstado(self) -> str:
        pass

    @abstractmethod
    def verificaEstado(self) -> None:
        pass