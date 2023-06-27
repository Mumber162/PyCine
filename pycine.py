#--------------------------------
import movies
import clients
import users
#================================


#== CRUDs ===
def filmes():
    # Lista de Filmes
    films_dict = []

    status = True
    while status:
        print("\n===============================")
        print("== FILMES em DESENVOLVIMENTO ==")
        print("...............................")
        print("[1] - Cadastrar                ")
        print("[2] - Buscar                   ")
        print("[3] - Atualizar                ")
        print("[4] - Remover                  ")
        print("[5] - VER Filmes               ")
        print("(0) - Sair                     ")
        print("-------------------------------")

        opt = int(input("\t=> "))

        if opt==1:
            movies.register(films_dict)
        elif opt==2:
            movies.search(films_dict)
        elif opt==3:
            movies.update_film(films_dict)
        elif opt==4:
            movies.remove_film(films_dict)
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
    O filme vai ter como atributos:
    - Nome, gênero(s), diretor(es), ano de lançamento, classif. indicativa, duração
    """


def clientes():
    """
    Os clientes vão ter como atributos:
    - Nome, idade
    E os ingressos serão gerados a partir deles
    """

    # Lista de Clientes
    clients_dict = []

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


        opt = int(input("\t=> "))

        if opt==1:
            clients.register(clients_dict)
        elif opt==2:
            clients.search(clients_dict)
        elif opt==3:
            clients.update_client(clients_dict)
        elif opt==4:
            clients.remove_client(clients_dict)
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
    # Lista de Ingressos
    tickets_dict = []

    """
    Acredito que terá:
    - numero do ingresso (equivalente a quantidade de poltronas)
    - nome do cliente que adquiriu o ingresso
    - data e hora da sseão
    - poltrona

    Eles não possuem menu, pois são acessados por clientes, como se fosse
    uma chave estrangeira
    """

def usuarios():
    # Lista de Usuários
    users_dict = []

    status = True
    while status:

        print("\n=================================")
        print("== USUÁRIOS em DESENVOLVIMENTO ==")
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
            users.remove_user(users_dict)
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

    """
    Admin, funcionario
    - Nome, cargo
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
    print("\nwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    print("          Bem-Vindo ao        ")
    print("          P Y C I N E         ")
    print("------------------------------")
    print("======== VOCÊ DESEJA =========")
    print("# [1] - Aba Filmes            ")
    print("# [2] - Aba Clientes          ")
    print("# [3] - Aba Ingressos         ")
    print("# [4] - Aba Usuários          ")
    print("# [5] - Relatórios            ")
    print("  (0) - Sair                  ")
    print("------------------------------")

status = True
while status:
    home()
    resp = input("Escolha -> ")

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