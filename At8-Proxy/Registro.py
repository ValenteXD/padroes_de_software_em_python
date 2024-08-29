class Registro:
    def __init__(self,list_auth:list[str],content:str) -> None:
        self.__authorized = list_auth
        self.__content = content
    def getContent(self,id):
            if self.__authorized.__contains__(id):
                return self.__content
            else:
                return "Acesso negado"
