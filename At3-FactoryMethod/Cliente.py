from CharacterFactory import CharacterFactory
if __name__=="__main__":
    factory = CharacterFactory()
    cura = factory.createHealer()
    tanque = factory.createPaladin()
    print("3 Slimes aparecem")
    tanque.atk()
    cura.defend()
    for i in range(3):
        print("Slime",i,"ataca o paladino")
    print("paladino está com pouca vida")
    tanque.defend()
    cura.atk()