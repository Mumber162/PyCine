#--------------------------------

# Verfica se tem clientes
def tem_client(clients_dict):
    if not clients_dict:
        print(" _____________________________ ")
        print("|  NÃO HÁ CLIENTES CADASTRADOS  |")
        print(" =---------------------------= ")

        input("Tecle ENTER para continuar...\n\n")

        return False
    else:
        return True
    
#================================

""""""
# CADASTRAR Clientes
""""""
def register():
    print("#####################\n|")

    name = input("| NOME: ")
    age  = input("| IDADE: ")
    cpf  = input("| CPF: ")

    client = {
        "name": name,
        "age":  age,
        'cpf': cpf,
    }
    
    return client


""""""
# BUSCAR Clientes
""""""
def search(clients_dict):
    
    ha_client = tem_client(clients_dict)
    if (ha_client):
        print("\n###############################")
        name_search = input("Digite o CPF do Cliente: ")

        print("========- RESULTADO -=======\n")
        if name_search in clients_dict.keys():
            print(clients_dict[name_search])

        else:
            print(" Não há clientes cadastrados com esse CPF\n")
       
        print("################################\n")
        input("Tecle ENTER para continuar...\n\n")


""""""
# ATUALIZAR
""""""
def update_client(clients_dict):

    ha_cliente = tem_client(clients_dict)
    if (ha_cliente):
        
        print("\n##################################")
        cliente = input("Qual cliente atualizar? ")

        print(f"... Atualizando {cliente} ...")
        atualiza = register()
        clients_dict[cliente] = atualiza


""""""
# VER
""""""
def see_all(clients_dict):
    print("___________________________")
    for ckey in clients_dict:
        print("\n----=== - CLIENTE  - ===----")
        print()
        print("NOME: ",  clients_dict[ckey]["name"])
        print("IDADE: ", clients_dict[ckey]["age"])
        print("CPF: ",   clients_dict[ckey]["cpf"])
    print("___________________________")
    input("Tecle ENTER para continuar...\n\n")
