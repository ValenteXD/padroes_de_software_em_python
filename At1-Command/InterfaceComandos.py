from abc import ABC, abstractmethod

#esta é a interface de comandos
class InterfaceComandos(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def desfaz(self):
        pass