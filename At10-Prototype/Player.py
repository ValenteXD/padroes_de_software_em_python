from colorama import Fore, Back, Style
from random import randint as rnd
class Player:
    def __init__(self) -> None:
        self.__health = 1000
        self.__atk = 25
    
    def atk(self):
        if rnd(1,10)==10:
            print(Fore.RED,Back.YELLOW,"GOLPE CRITICO!!!",Style.RESET_ALL)
            return self.__atk*5
        return self.__atk+rnd(-3,3)

    def hit(self,dmg):
        self.__health -= dmg

    def getHP(self):
        return "HP: "+str(self.__health)