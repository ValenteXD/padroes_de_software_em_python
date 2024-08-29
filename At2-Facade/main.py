from Fachada import Fachada
if __name__=="__main__":

    while True:
        print("Bem-vindo à agência gangue dos quatro, no que podedmos ajudar você?")
        print("digite 'explorar' para ver opções de destino")
        print("caso queira sair digite 'sair'")
        comando = input("insira um comando: ")
        if comando == "sair":
            break
        elif comando == "explorar":
            Fachada.destinos()
        else:
            print("comando não reconhecido\n")
    print("\nAté a próxima! :)")