from Paladin import Paladin
from Healer import Healer
class CharacterFactory:
    def createPaladin(self):
        paladin = Paladin()
        return paladin
    
    def createHealer(self):
        healer = Healer()
        return healer