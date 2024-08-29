import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
from colorama import Fore, Back, Style
from Enemy import Enemy
from Player import Player
from random import randint as rng
class Battlefield:
    def __init__(self) -> None:
        self.__len = 60
        self.__border = "="*self.__len
        self.__nmeList: list[Enemy] = []
        self.__baseEnemy = Enemy()
        self.__player = Player()
        rnd = 1
        for i in range(rng(2,5)):
            rnd = rng(1,5)
            self.__nmeList.append(self.__baseEnemy.clone(rnd))

    def distribute_strings(max_length, strings):
        total_chars = sum(len(s) for s in strings)
        num_strings = len(strings)
        space_needed = max_length - total_chars
        space_per_side = space_needed // num_strings
        extra_space = space_needed % num_strings
        
        distributed_strings = []
        for i, s in enumerate(strings):
            distributed_strings.append(" " * space_per_side)
            distributed_strings.append(s)
            distributed_strings.append(" " * space_per_side)
            if extra_space > 0:
                distributed_strings.append(" ")
                extra_space -= 1
        return ''.join(distributed_strings)

    def render(self):
        #calcula espaçamento de inimigos
        occupied:int = len(self.__nmeList)
        blank:int = self.__len-4
        gap:int=(blank-occupied*4)//(occupied+1)-1
        #criando array de HP
        health = []
        for e in self.__nmeList:
            health.append(e.getHP())
        #borda superior
        print(self.__border)
        #renderizando inimigos
        print("||",end="")
        for e in self.__nmeList:
            print(" "*gap,end="")
            e.render()
        print(" "*gap,end="")
        print("||")

        #borda inferior
        print(self.__border)
        #HP dos inimigos
        for i,e in enumerate(self.__nmeList):
            print(i,"->",e.getHP())

        #HP do jogador
        print("\nHerói ->",self.__player.getHP())

    def logic(self):
        #selecionando alvo
        while True:
            try:
                target = min(max(int(input("\nEscolha um inimigo para atacar: ")),0),len(self.__nmeList)-1)
                break
            except:
                print("um número por favor")
        #causando dano ao inimigo
        dmg = self.__player.atk()
        self.__nmeList[target].hit(dmg)
        print("O inimigo recebeu",dmg,"de dano")
        #verificando nocautes
        for i,e in enumerate(self.__nmeList):
            if int(e.getHP()[4:])<=0:
                self.__nmeList.pop(i)
                print("Inimigo derrotado!")
        #verificando vitória
        if len(self.__nmeList)==0:
            print(Fore.YELLOW,"Parabéns!! Os inimigos foram todos derrotados!",Style.RESET_ALL)
            quit()
        #causando dano ao jogador
        for e in self.__nmeList:
            dmg=e.atk()
            self.__player.hit(dmg)
            print("Você recebeu",dmg,"de dano")

        #verificando se jogador está vivo
        if int(self.__player.getHP()[4:])<=0:
            print(Fore.RED,"Você foi derrotado",Style.RESET_ALL)
            quit()
        