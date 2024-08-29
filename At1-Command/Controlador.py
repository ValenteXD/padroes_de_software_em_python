from Luz import ControlaLuz
from TV import *

#Este é o Invoker no padrão de comandos
class Controlador:
    # cria hitórico e dicionário de comandos estático
    __historico__=[]
    __comandos__ = {
        "luz": ControlaLuz(),
        "aumentaTV":AumentaVolume(),
        "diminuiTV":DiminuiVolume(),
        "ligaTV":LigaTV(),
        "desligaTV":DesligaTV(),
        "mudaCanal":MudarCanal(),
    }

    def invoke(self,comando):
        #verifica se comando existe
        if list(Controlador.__comandos__.keys()).count(comando)!=0:
            Controlador.__comandos__[comando].execute()
            Controlador.__historico__.append(comando)
        else:
            print("comando não encontrado, tente digitar 'ajuda' para ver lista de comandos")

    def desfazer(self):
        
        if Controlador.__historico__:
            comando = Controlador.__historico__.pop()
            print("O comando " + comando + " foi desfeito")
            Controlador.__comandos__[comando].desfaz()
        else:
            print("sem comandos para desfazer")

    #melhora a experiência do usuário
    def ajuda(self):
        print("Comandos disponíveis:")
        for key in list(Controlador.__comandos__.keys()):
            print(key)
        print("desfazer")
        print("ajuda")
        print("sair")
        print("")