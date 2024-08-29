from colorama import Fore, Back, Style
from random import randint as rnd

class Enemy:
    def __init__(self,lvl=1,health=50,atk=10) -> None:
        self.__level = lvl
        self.__health:int = health
        self.__atk:int = atk
    
    colormap = {
        1:Back.BLACK,
        2:Back.GREEN,
        3:Back.LIGHTBLUE_EX,
        4:Back.WHITE,
        5:Back.YELLOW,
    }

    def getHP(self):
        return "HP: "+str(self.__health)

    def atk(self):
        if rnd(1,10)<=8:
            return self.__atk+rnd(-3,3)
        return 0
    
    def hit(self,dmg:int):
        self.__health-=dmg

    def render(self):
        print(Enemy.colormap[self.__level]+" 👻  "+Style.RESET_ALL,end="")

    def clone(self,level:int):
        lvl = max(min(level,5),0)
        atk = self.__atk*level
        health = self.__health+level*10
        return Enemy(lvl,health,atk)