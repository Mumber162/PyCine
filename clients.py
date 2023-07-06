#--------------------------------
import library.check_cpf as check

# Verfica se tem clientes
def tem_client(clients_dict):
    if not clients_dict:
        print(" _______________________________ ")
        print("|  NÃO HÁ CLIENTES CADASTRADOS  |")
        print(" =-----------------------------= ")

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
    tel  = input("| TELEFONE: ")

    invalid = True
    while invalid:
        cpf  = input("| CPF: ")

        if (check.validar_cpf(cpf)):
            print("CPF Válido!... ")
            invalid = False
        else:
            print("CPF INVÁLIDO!")

    client = {
        "name": name,
        "age":  age,
        "phone": tel,
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

        return atualiza


""""""
# VER
""""""
def see_all(clients_dict):

    ha_client = tem_client(clients_dict)
    if (ha_client):
        print("___________________________")
        for ckey in clients_dict:
            print("\n----=== - CLIENTE  - ===----")
            print()
            print("NOME: ",     clients_dict[ckey]["name"])
            print("IDADE: ",    clients_dict[ckey]["age"])
            print("TELEFONE: ", clients_dict[ckey]["phone"])
            print("CPF: ",      clients_dict[ckey]["cpf"])
        print("\n")
        input("Tecle ENTER para continuar...\n\n")
