from InterfaceComandos import InterfaceComandos

class Televisao:
    volume = 0
    def aumentar():
        Televisao.volume += 1
        Televisao.volume = min(10,Televisao.volume)
        return Televisao.volume
    def reduzir():
        Televisao.volume -= 1
        Televisao.volume = max(0,Televisao.volume)
        return Televisao.volume
    def mudarCanal(canal):
        print("agora reproduzindo: ", end="")
        print(canal)
        if Televisao.canal is not None:
            Televisao.canalAntigo=Televisao.canal
        Televisao.canal=canal
    def voltarCanal():
        print("agora reproduzindo: ", end="")
        print(Televisao.canalAntigo)
        temp=Televisao.canalAntigo
        Televisao.canalAntigo=Televisao.canal
        Televisao.canal=temp
    
class LigaTV(InterfaceComandos):
    def execute(self):
        print("TV liga")
    
    def desfaz(self):
        print("TV desliga")

class DesligaTV(InterfaceComandos):
    def execute(self):
        print("TV desliga")

    def desfaz(self):
        print("TV liga")

class DiminuiVolume(InterfaceComandos):
    def execute(self):
        print("Volume da TV: ", end="")
        print(Televisao.reduzir())
    def desfaz(self):
        print("Volume da TV: ", end="")
        print(Televisao.aumentar())

class AumentaVolume(InterfaceComandos):
    def execute(self):
        print("Volume da TV: ", end="")
        print(Televisao.aumentar())
    def desfaz(self):
        print("Volume da TV: ", end="")
        print(Televisao.reduzir())

class MudarCanal(InterfaceComandos):
    def execute(self):
        canal=input("insira um canal: ")
        Televisao.mudarCanal(canal)
    def desfaz(self):
        Televisao.voltarCanal()