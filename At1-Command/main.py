from Controlador import Controlador

#main
if __name__=="__main__":
    assistente = Controlador()
    assistente.ajuda()
    while True:
        comando = input("digite um comando: ")
        if comando == "sair":
            break
        if comando == "ajuda":
            assistente.ajuda()
        elif comando == "desfazer":
            assistente.desfazer()
        else:
            assistente.invoke(comando)
