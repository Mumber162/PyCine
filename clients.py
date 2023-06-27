# CADASTRAR
def register(clients_dict):
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print("|")

    name = input("| NOME: ")
    age  = input("| IDADE: ")

    client = {
        "name": name,
        "age":  age,
        "ticket_number": (len(clients_dict))
    }

    clients_dict.append(client)

# VER
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