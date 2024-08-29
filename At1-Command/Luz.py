from InterfaceComandos import InterfaceComandos

class ControlaLuz(InterfaceComandos):
    luz = False

    def execute(self):
        ControlaLuz.luz = not ControlaLuz.luz
        if ControlaLuz.luz:
            print("luz acende")
        else:
            print("luz apaga")

    def desfaz(self):
        self.execute()