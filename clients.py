#--------------------------------
import tickets
import movies
#================================


""""""
# CADASTRAR Clientes
""""""
def register(clients_dict, films_dict):
    print("#####################\n|")

    name = input("| NOME: ")
    age  = input("| IDADE: ")
    cpf  = input("| CPF: ")

    #------- Parte dos Clientes ============
    client = {
        "name": name,
        "age":  age,
        "ticket_number": (len(clients_dict))
    }
    
    clients_dict[cpf] = client

    #------- Parte dos INGRESSOS ===========
    print("\n=================================")
    print("==        MENU INGRESSOS        ==")
    print(".................................")
    print("[1] - Comprar Ingressos          ")
    print("[2] - Cancelar Ingressos         ")
    print("(0) - Sair                       ")
    print("---------------------------------")


    ha_filme = movies.tem_filme(films_dict)
    if (ha_filme):
        
        ingresso = {}


""""""
# BUSCAR Clientes
""""""
def search(clients):
    print()


""""""
# VER
""""""
def see_all(clients_dict):
    print("___________________________")
    for i in range(len(clients_dict)):
        print("\n----=== - CLIENTE %d - ===----" % (int(i)+1))
        print()
        print("NOME: ",         clients_dict[i]["name"])
        print("IDADE: ",        clients_dict[i]["age"])
        print("Nº de TICKET: ", clients_dict[i]["ticket_number"])
        print("- - - =-= - - - =-= - - -")
    print("___________________________")