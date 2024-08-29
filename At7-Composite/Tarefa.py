from typing import List

class Tarefa:
    def __init__(self, titulo) -> None:
        self.__concluida__ = False
        self.subTarefas: List[Tarefa] = []
        self._titulo = titulo
    
    def marcarConcluida(self) -> str:
        self.__concluida__ = True
        for sub in self.subTarefas:
            sub.marcarConcluida()
        return self._titulo + " concluida"

    def desmarcarConcluida(self) -> str:
        self.__concluida__ = False
        for sub in self.subTarefas:
            sub.desmarcarConcluida()
        return self._titulo + " marcada como não concluida"
    
    def novaTarefa(self, titulo) -> None:
        self.subTarefas.append(Tarefa(titulo=titulo))

    def consultar(self,nivel: int = 1) -> str:
        resultado = self._titulo
        resultado += " ✔"if self.__concluida__ else " □"
        for sub in self.subTarefas:
            resultado += "\n"+"│"*(nivel-1) + "└" + sub.consultar(nivel=nivel+1)
        return resultado

    def getSubTarefa(self,titulo:str):
        for sub in self.subTarefas:
            if sub._titulo == titulo:
                return sub
            else:
                inferior = sub.getSubTarefa(titulo=titulo)
                if type(inferior) != type(None):
                    return inferior
        return None