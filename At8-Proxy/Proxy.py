from IDatabase import IDatabase
from Database import DBprovider

class Proxy(IDatabase):

    def __init__(self) -> None:
        self.__db = DBprovider.getDB()
        
    def requestAccess(self, id:str, data:int) -> str:
        print(id+" requisitou acesso ao dado "+str(data))
        return self.__db.requestAccess(id=id,data=data)
    