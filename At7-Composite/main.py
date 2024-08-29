#João Pedro Covello Valente
#2122172BCC

from Tarefa import Tarefa
def help():
    print("\n\n1: consultar status de todas as tarefas\n2: Selecionar uma sub tarefa\n3: Marcar a tarefa seleciona e todas as suas sub tarefas como concluidas"+
          "\n4: Marcar a tarefa seleciona e todas as suas sub tarefas como não concluidas\n5: Selecionar a tarefa principal\n6: Menu de Ajuda\n7: sair")
    
if __name__=="__main__":
    tarefaPrincipal = Tarefa("Arrumar a casa")
    tarefaPrincipal.novaTarefa("arrumar quarto")
    tarefaPrincipal.novaTarefa("limpar banheiro")
    quarto = tarefaPrincipal.getSubTarefa("arrumar quarto")
    if isinstance(quarto,Tarefa):
        quarto.novaTarefa("arrumar cama")
        quarto.novaTarefa("organizar estante")
    estante = tarefaPrincipal.getSubTarefa("organizar estante")
    if isinstance(estante,Tarefa):
        estante.novaTarefa("ordenar livros por série")
        estante.novaTarefa("tirar o pó das prateleiras")
        estante.novaTarefa("guardar coleção de minifigures na prateleira mais alta")
    banheiro = tarefaPrincipal.getSubTarefa("limpar banheiro")
    if isinstance(banheiro,Tarefa):
        banheiro.novaTarefa("guardar os remédios na dispensa")
        banheiro.novaTarefa("lavar e secar a pia")
        banheiro.novaTarefa("trocar sabonetes")
        banheiro.novaTarefa("repor pasta de dente")
    print("Olá! Você tem uma lista de tarefas atribuída\n")
    print(tarefaPrincipal.consultar())
    tarefaAtual:Tarefa = tarefaPrincipal
    help()
    while True:
        try:
            entrada = int(input("digite o número do comando: "))
        except:
            print("ERRO! Comando não numérico")
            continue
        match entrada:
            case 1:
                print(tarefaPrincipal.consultar())
                continue
            case 2:
                aux = tarefaPrincipal.getSubTarefa(input("digite exatamente o nome da tarefa que gostaria de acessar: "))
                if type(aux) == type(None):
                    print("não conseguimos recuperar sua tarefa")
                else:
                    tarefaAtual = aux
                    print("Tarefa " + tarefaAtual._titulo + " selecionada com sucesso!")
                continue
            case 3:
                print(tarefaAtual.marcarConcluida())
                continue
            case 4:
                print(tarefaAtual.desmarcarConcluida())
                continue
            case 5:
                tarefaAtual = tarefaPrincipal
                print("Tarefa " + tarefaAtual._titulo + " selecionada com sucesso!")
                continue
            case 6:
                help()
                continue
            case 7:
                break
            case _:
                print("ERRO! Comando inexistente")