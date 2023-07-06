#--------------------------------
import pickle
import users
#================================

# Printa as opções de filmes
def opcoes(films_dict):
    print("\n#########  TEMOS  ##########\n")

    # Forma otimizada de printar elementos de dicionários dentro de dicionários
    keys = films_dict.values()
    for k in keys:
        print(f"Título: {k['title']} ({k['release']})")
        print(f"[COD.]: {k['code']}")

    print("\n===========================")

# Verfica se tem filmes ou não
def tem_filme(films_dict):
    if not films_dict:
        print(" _____________________________ ")
        print("|  NÃO HÁ FILMES CADASTRADOS  |")
        print(" =---------------------------= ")

        input("Tecle ENTER para continuar...\n\n")

        return False
    else:
        return True

""""""
# CADASTRAR Filmes
""""""
def register():
    print("\n#######################################")
    print("|-(se tiver + de 1, separe por vírgula)--")
    print("|")

    title     = input("| TÍTULO do filme: ")
    genre     = input("| GÊNERO(s): ")
    director  = input("| DIRETOR(es): ")
    release   = input("| DATA de Lançamento: ")
    class_ind = input("| Classificação Indicativa: ")
    duration  = int(input("| Duração (em min): "))
    code      = input("(Código do Filme): ").upper()

    genres = genre.split(", ")
    directors = director.split(", ")

    movie = {
        'code':      code,
        "title":     title,
        "genre":     genres,
        "director":  directors,
        "release":   release,
        "class_ind": class_ind,
        "duration":  duration
        }
    return movie

""""""
# BUSCAR
""""""
def search(films_dict):

    ha_filme = tem_filme(films_dict)
    if (ha_filme):
        print("\n###############################")
        s = input("Digite o código do filme: ").upper()

        print("========- RESULTADO -=======\n")
        for key in films_dict.keys():
            if (s in key):
                print(f"1: {films_dict[s]['title']} | Lançamento: {films_dict[s]['release']}\n")

            else:
                print(" Não há filmes cadastrados com esse título\n")
       
        print("################################\n")
        input("Tecle ENTER para continuar...\n\n")

""""""
# ATUALIZAR
""""""
# if (users.verifica_cargo())
def update_film(films_dict):

    ha_filme = tem_filme(films_dict)
    if (ha_filme):
        opcoes(films_dict)
        print(" #  - Qual filme atualizar [dgt o código]")
        print("(0) - Cancelar")
        filme = input("-> : ").upper()

        if (filme) in films_dict.keys():

            print("\n#######################################")
            print(f"    ... Atualizando {filme} ...")
            print("Para atualizar TUDO, digite [T]")
            print("P/ atualizar só uma chave específica, dgt em inglês")
            print("#######################################")
            upd = input("-> ")


            if upd.upper()=="T":
                movie = register()
                movie['code'] = filme

                return movie

            elif upd in films_dict[filme].keys():
                print("|-(se tiver + de 1, separe por vírgula)--")
                print("|")

                print(f"New {upd}: ", end="")
                if upd!="duration":
                    val = input()
                else:
                    val = int(input())

                films_dict[filme][upd] = val

                movie = films_dict[filme]
                return movie

            else:
                print("\n => Update Cancelado!")
        else:
            print("\n => Update Cancelado! (ou não tem filmes com esse título)")
        input("Tecle ENTER para continuar...\n\n")

""""""
# REMOVER
""""""
def delete_film(films_dict):

    ha_filme = tem_filme(films_dict)
    if (ha_filme):
        # Printa as opções de filmes
        print("\n########################")
        print("Qual filme quer deletar:")
        print("........................", end="")
        opcoes(films_dict)

        option = input("[Dgt o título] -> ").upper()
        del films_dict[option]

        # "Deletando" do Banco
        arqFilmes = open('database/movies_db.dat', 'wb')
        pickle.dump(films_dict, arqFilmes)
        arqFilmes.close()

        print("= Filme Deletado com Sucesso!")
        input("Tecle ENTER para continuar...\n\n")


""""""
# VER
""""""
def see_all(films_dict):

    ha_filme = tem_filme(films_dict)
    if (ha_filme):

        keys = films_dict.values()
        for fk in (keys):
            print(f"\n== • Filme: {(fk['title']).upper()} • ==\n")

            print("GÊNERO(s): \n•", end="")
            for gnr in fk['genre']:
                print("", gnr, end=" -")
            print()
            print("DIRETOR(es):", end="")
            for dir in fk['director']:
                print("", dir, end=" -")

            print("\nDATA DE LANÇAMENTO: ", fk["release"])
            print("CLASSIF. INDICATIVA: ",  fk["class_ind"])

            hora    = (fk["duration"])//60
            minutos = (fk["duration"])%60
            print(f"DURAÇÃO: {hora}h {minutos}min\n--------------------------")

        input("Tecle ENTER para continuar...\n\n")