import time

class Hotel:
    def __init__(self,nome,vagas,custo):
        self.nome=nome
        self.vagas=vagas
        self.custo=custo
class Viagens:
    destinos = {
        "Orlando":{"hotel_1":Hotel("Dineyland",0,1000000),"hotel_2":Hotel("Tropical Horizon",0,300000),"hotel_3":Hotel("Sunset Refugee",0,230000),"hotel_4":Hotel("Coast Cruisers",0,800000),"hotel_5":Hotel("Empiricals",0,20000000),},
        "Acapulco":{"hotel_1":Hotel("El Refugio",1,920000),"hotel_2":Hotel("Las Playas",0,500000),"hotel_3":Hotel("El Legado",0,340000),},
        "Natal":{"hotel_1":Hotel("Brisa Mar",2,60000),"hotel_2":Hotel("Areias Divinas",8,130000),},
    }
    def verDestinos():
        #recupera destinos disponibilizados pela agência
        return list(Viagens.destinos.keys())
    def verHoteis(destino):
        #recupera lista de hotéis com convênio com a agência no destino requisitado
        lista=[]
        for hotel in Viagens.destinos[destino].keys():
            lista.append(Viagens.destinos[destino][hotel])
        return lista
    def pagamento(metodo):
        #lógica complexa para aprovar pagamento
        print("0%",end="\r")
        time.sleep(4)
        print("3%",end="\r")
        time.sleep(4)
        print("15%",end="\r")
        time.sleep(4)
        print("40%",end="\r")
        time.sleep(4)
        print("80%",end="\r")
        time.sleep(4)
        print("99%",end="\r")
        time.sleep(14)
        print("100%",end="\r")
        return True
    def reservar(destino,id):
        #retorna objeto com dados do hotel acessados na base de dados
        return Viagens.destinos[destino][id]

