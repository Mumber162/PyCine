#--------------------------------
import movies
import clients
import users
import webbrowser
#================================

# Listas
films_dict = []
clients_dict = []
tickets_dict = []
users_dict = []

#== CRUDs ===
def filmes():

    status = True
    while status:
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

        opt = int(input("Resposta => "))

        if opt==1:
            movies.register(films_dict)
        elif opt==2:
            movies.search(films_dict)
        elif opt==3:
            movies.update_film(films_dict)
        elif opt==4:
            movies.delete_film(films_dict)
        elif opt==5:
            movies.see_all(films_dict)
        elif opt==0:
            print("\n")        
            print("=== OBRIGADO PELA VISITA nos FILMES! ===")
            print("\n")
            status = False
        else:
            print("\t|    INVALIDO   |")
            print("\t| Tente de novo |")

    """
    [Atributos]:
        - Nome,
        - gênero(s),
        - diretor(es),
        - ano de lançamento,
        - classif. indicativa,
        - duração (min)
    """


def clientes():

    """
    [Atributos]:
        - Nome, idade (pra ver se pode assistir)
        - Ingressos (serão gerados a partir dos clientes)
    """

    status = True
    while status:

        print("\n=================================")
        print("== CLIENTES em DESENVOLVIMENTO ==")
        print(".................................")
        print("[1] - Cadastrar                  ")
        print("[2] - Buscar                     ")
        print("[3] - Atualizar                  ")
        print("[4] - Remover                    ")
        print("[5] - VER Clientes               ")
        print("(0) - Sair                       ")
        print("---------------------------------")


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
    [Atributos]- Nome, cargo
    (Cargos)
        - Admin (gerente)
        - Funcionário Comum

        Se o usuário for ADMIN, ele pode:
            # remover, alterar e editar os filmes;
            # remover, alterar e editar os funcionários;
        Se o user foi COMUM, ele pode apenas ver os filmes e funcionários;
    """

def relatorios():
    print("\n== Aqui está o relatório ==")
    print("==== De Todo o CINEMA =====")
    print("...........................")
    print()
    

#
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
    print("\t# [2] - Aba Clientes          ")
    print("\t# [3] - Aba Ingressos         ")
    print("\t# [4] - Aba Usuários          ")
    print("\t# [5] - Relatórios            ")
    print("\t  (0) - Sair                  ")
    print("\t------------------------------")

status = True
while status:
    home()
    resp = input("\tEscolha -> ")

    if resp=="1":
        filmes()
    elif resp=="2":
        clientes()
    elif resp=="3":
        ingressos()
    elif resp=="4":
        usuarios()
    elif resp=="5":
        relatorios()

    elif resp=="0":
        print("\n")
        print("=== OBRIGADO PELA VISITA! ===")
        print("\n")
        status = False

    else:
        print("\n")
        print("=================")
        print("|    INVALIDO   |")
        print("| Tente de novo |")
        print("=================")
        print("\n")