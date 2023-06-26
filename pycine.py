#--------------------------------
import movies
#================================


#== CRUDs ===
def filmes():
    films_dict = []

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

    opt = int(input("=> "))

    status = True
    while status:
        if opt==1:
            movies.register(films_dict)
        if opt==2:
            movies.search()
        if opt==3:
            movies.update_film()
        if opt==4:
            movies.remove_film()
        if opt==0:
            print("OBRIGADO PELA VISITA nos FILMES!")
            status = False

        else:
            print("|    INVALIDO   |")
            print("| Tente de novo |")

    """
    O filme vai ter como atributos:
    - Nome, gênero(s), diretor(es), ano de lançamento, classif. indicativa, duração
    """


def clientes():
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

    """
    Os clientes vão ter como atributos:
    - Nome, idade
    """


def ingressos():
    print("\n==================================")
    print("== INGRESSOS em DESENVOLVIMENTO ==")
    print("..................................")
    print("[1] - Cadastrar                   ")
    print("[2] - Buscar                      ")
    print("[3] - Atualizar                   ")
    print("[4] - Remover                     ")
    print("[5] - VER Ingressos               ")
    print("(0) - Sair                        ")
    print("----------------------------------")

    """
    Acredito que terá:
    - numero do ingresso (equivalente a quantidade de poltronas)
    - nome do cliente que adquiriu o ingresso
    - data e hora da sseão
    - poltrona
    """

def usuarios():
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
    """
    Admin, funcionario
    - Nome, cargo
    """

def relatorios():
    print("\n== Aqui está o relatório ==")
    print("==== De Todo o CINEMA =====")
    print("...........................")

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
        print("OBRIGADO PELA VISITA!")
        status = False

    else:
        print("|    INVALIDO   |")
        print("| Tente de novo |")