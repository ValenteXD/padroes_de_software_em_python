from Context import Context
if __name__=="__main__":
    context = Context()
    context.exec()
    print("Tente um desses comandos: ",end="")
    for key in context.__comandos__.keys():
        print(key,", ",end="")
    print("quando decidir a estrategia digite 'acao'")
    print("Caso queira fechar o programa digite 'sair'")
    while True:
        entrada = input("Digite um comando: ")
        if context.__comandos__.__contains__(entrada):
            context.setStrategy(entrada)
        else:
            if entrada == "sair":
                break
            elif entrada == "acao":
                context.exec()
            else:
                print("As tropas estão confusas com a sua ordem")
                print("Tente um desses comandos: ",end="")
                for key in context.__comandos__.keys():
                    print(key,", ",end="")
                print("quando decidir a estrategia digite 'acao'")
                print("Caso queira fechar o programa digite 'sair'")