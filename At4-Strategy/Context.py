from Offense import Offense
from Retreat import Retreat
from Stealth import Stealth
from Standby import Standby

class Context:
    __comandos__ = {
        "aguarde": Standby(),
        "ofensiva": Offense(),
        "recuar": Retreat(),
        "furtivo": Stealth(),
    }

    def __init__(self):
        self.__estrategia__ = "aguarde"
        
    def setStrategy(self,strat: str):
        self.__estrategia__ = strat
        print("estrategia alterada para "+strat)

    def exec(self):
        Context.__comandos__[self.__estrategia__].exec()
    