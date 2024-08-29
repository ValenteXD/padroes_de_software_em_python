from IDatabase import IDatabase
from Registro import Registro
class Database(IDatabase):
    def __init__(self, dataset: dict[int,Registro]) -> None:
        self.data = dataset

    def requestAccess(self,id:str, data:int) ->str:
        if self.data.keys().__contains__(data):
            return self.data[data].getContent(id=id)
        else:
            return "dado inexistente"
    
class DBprovider:
    __db = Database({1:Registro(["Marcelo","Jorge"],"Essa msg é sigilosa"),
                   2:Registro(["João Pedro","Marcelo","Jorge"],"Essa msg é mais amplamente acessível")})
    def getDB()-> Database:
        return DBprovider.__db