from Proxy import Proxy
if __name__=="__main__":
    acesso = Proxy()
    print(acesso.requestAccess("João Pedro",1),'\n') # Deve retornar acesso negado pois não esá lista de autorizados
    print(acesso.requestAccess("Jorge",1),'\n') # Deve retornar a msg sigilosa guardada na database
    print(acesso.requestAccess("João Pedro",2),'\n') # Deve retornar a msg pois 'João Pedro' tem acesso
    print(acesso.requestAccess("Marcelo",2),'\n') # Assim como Marcelo
    print(acesso.requestAccess("Zé ninguém",2),'\n') # Mas ainda não aberta à todos 
    try:
        print(acesso.__db.data[1].__content) # haverá um erro de atributo pois a Proxy não expõe a database
    except AttributeError:
        print("Erro! Não dá pra acessar diretamente")