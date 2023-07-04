#--------------------------------
import movies
import clients
import tickets
import users
import webbrowser
#================================


def menu_filmes():
    print("\n===============================")
    print("==        MENU FILMES        ==")
    print("...............................")
    print("[1] - Cadastrar                ")
    print("[2] - Buscar                   ")
    print("[3] - Atualizar                ")
    print("[4] - Remover                  ")
    print("[5] - VER Filmes               ")
    print("(0) - Sair                     ")
    print("-------------------------------")
def menu_ingressos():
    print("\n=================================")
    print("==        MENU INGRESSOS       ==")
    print(".................................")
    print("[1] - Comprar                    ")
    print("[2] - Buscar                     ")
    print("[3] - Atualizar                  ")
    print("[4] - Remover                    ")
    print("[5] - VER Ingressos              ")
    print("(0) - Sair                       ")
    print("---------------------------------")
def menu_clientes():
    print("\n=================================")
    print("==        MENU CLIENTES        ==")
    print(".................................")
    print("[1] - Cadastrar                  ")
    print("[2] - Buscar                     ")
    print("[3] - Atualizar                  ")
    print("[4] - Remover                    ")
    print("[5] - VER Clientes               ")
    print("(0) - Sair                       ")
    print("---------------------------------")

# Listas
films_dict = {}
clients_dict = {}
tickets_dict = {}
users_dict = {}

#== CRUDs ===
def filmes():
    status = True
    while status:
    
        menu_filmes()
        opt = int(input("Resposta => "))

        if opt==1:
            movie = movies.register()
            films_dict[(movie['code'])] = movie
        elif opt==2:
            movies.search(films_dict)
        elif opt==3:
            movies.update_film(films_dict)
        elif opt==4:
            movies.delete_film(films_dict)
        elif opt==5:
            movies.see_all(films_dict)
        elif opt==0:
            print("\n\n=== OBRIGADO PELA VISITA nos FILMES! ===\n\n")
            status = False
        else:
            print("\t|    INVALIDO   |")
            print("\t| Tente de novo |")


def clientes():
    status = True
    while status:

        menu_clientes()
        opt = int(input("Resposta=> "))

        if opt==1:
            clients.register(clients_dict, films_dict)
        elif opt==2:
            clients.search(clients_dict)
        elif opt==3:
            clients.update_client(clients_dict)
        elif opt==4:
            clients.delete_client(clients_dict)
        elif opt==5:
            clients.see_all(clients_dict)
        elif opt==0:
            print("\n")        
            print("=== OBRIGADO PELA VISITA nos CLIENTES! ===")
            print("\n")
            status = False
        else:
            print("\t|    INVALIDO   |")
            print("\t| Tente de novo |")


def ingressos():
    status = True
    while status:

        menu_clientes()
        opt = int(input("Resposta=> "))

        if opt==1:
            tickets.register(clients_dict, films_dict)
        elif opt==2:
            clients.search(clients_dict)
        elif opt==3:
            clients.update_client(clients_dict)
        elif opt==4:
            clients.delete_client(clients_dict)
        elif opt==5:
            clients.see_all(clients_dict)
        elif opt==0:
            print("\n")        
            print("=== OBRIGADO PELA VISITA nos CLIENTES! ===")
            print("\n")
            status = False
        else:
            print("\t|    INVALIDO   |")
            print("\t| Tente de novo |")
    """
    [Atributos]:
        - Nº do ingresso (equivalente a quantidade de poltronas)
        - nome do cliente que adquiriu o ingresso
        - data e hora da sessão
        - filme
        - "poltrona (?)"

        Eles não possuem menu, pois são acessados por clientes, como se fosse
        uma chave estrangeira
    """

# -= Para desenvolver Futuramente...
# Aba de "Usuários"
"""
def usuarios():

    status = True
    while status:

        # Se não tiver nenhum usuário cadastrado
        if (len(users_dict)==0):
            print("\n=================================")
            print("==        MENU USUÁRIOS        ==")
            print(".................................")
            print("[1] - Cadastrar                  ")
            print("(0) - Sair                       ")
            print("---------------------------------")

            opt = int(input("Resposta => "))

            if opt==1:
                users.register(users_dict)
            elif opt==0:
                print("\n")        
                print("=== OBRIGADO PELA VISITA nos USUÁRIOS! ===")
                print("\n")
                status = False
            else:
                print("\t|    INVALIDO   |")
                print("\t| Tente de novo |")

        # Se tiver algum usuário cadastrado
        else:
            admin = users.verifica_admin(users_dict)

            # Se for [ADMIN]
            if (admin):
                print("\n=================================")
                print("==        MENU USUÁRIOS        ==")
                print(".................................")
                print("[1] - Cadastrar                  ")
                print("[2] - Buscar                     ")
                print("[3] - Atualizar                  ")
                print("[4] - Remover                    ")
                print("[5] - VER Usuários               ")
                print("(0) - Sair                       ")
                print("---------------------------------")

                opt = int(input("\t=> "))

                if opt==1:
                    users.register(users_dict)
                elif opt==2:
                    users.search(users_dict)
                elif opt==3:
                    users.update_user(users_dict)
                elif opt==4:
                    users.delete_user(users_dict)
                elif opt==5:
                    users.see_all(users_dict)
                elif opt==0:
                    print("\n")        
                    print("=== OBRIGADO PELA VISITA nos USUÁRIOS! ===")
                    print("\n")
                    status = False
                else:
                    print("\t|    INVALIDO   |")
                    print("\t| Tente de novo |")
                
            else:
                # Se for [comum]
                print()

"""

def relatorios():
    print("\n== Aqui está o relatório ==")
    print("==== De Todo o CINEMA =====")

    print(films_dict)
    print(clients_dict)

    print("...........................")
    print()
    
#
##########################
#=- PROGRAMA PRINCIPAL -=#
##########################

def home():
    print("\n\twwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    print("\t          Bem-Vindo ao        ")
    print("\t          P Y C I N E         ")
    print("\t------------------------------")
    print("\t======== VOCÊ DESEJA =========")
    print("\t# [1] - Aba Filmes            ")
    print("\t# [2] - Comprar Ingressos     ")
    print("\t# [3] - Aba Clientes          ")
#   print("\t# [5] - Relatórios            ")
    print("\t  (0) - Sair                  ")
    print("\t------------------------------")

main = True
while main:
    home()
    resp = input("\tEscolha -> ")

    if resp=="1":
        filmes()
    elif resp=="2":
        ingressos()
    elif resp=="3":
        clientes()

    elif resp=="0":
        print("\n\n=== OBRIGADO PELA VISITA! ===\n\n")
        main = False

    else:
        print("\n=================")
        print("|    INVALIDO   |")
        print("| Tente de novo |")
        print("=================\n\n")