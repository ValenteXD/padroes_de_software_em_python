from CentralDePedidos import CentralDePedidos
import time
if __name__=="__main__":
    pedido = CentralDePedidos()
    time.sleep(2)
    while True:
        entrada = input("O que pretende fazer?\n1 - Esperar\n2 - Verificar status do pedido\n3 - Fechar aplicativo\n\n")
        try:
            entrada = int(entrada)
            match entrada:
                case 1:
                    pedido.updateStatus()
                case 2:
                    pedido.checkStatus()
                case 3:
                    print("Aplicativo fecha")
                    break
                case _:
                    raise Exception()
        except:
            print("Um erro ocorreu, digite um número entre 1 e 3 por favor")
        time.sleep(2)
