#--------------------------------
import pickle
import users
#================================

# Printa as opções de filmes
def opcoes(films_dict):
    print("\n######  TEMOS  ########\n")
    for chave in films_dict.keys():
        print(f"Título: {films_dict[chave]['title']} ({films_dict[chave]['release']})")

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

    genres = genre.split(", ")
    directors = director.split(", ")

    movie = {
        'code':      title.upper(),
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
        name_search = input("Digite o nome do filme: ").upper()

        print("========- RESULTADO -=======\n")
        if name_search in films_dict.keys():
            print(f"1: {films_dict[name_search]['title']} | Lançamento: {films_dict[name_search]['release']}\n")

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
        print("\n##################################")
        filme = input("Qual filme atualizar [dgt o título]? ").upper()

        if (filme.upper()) in films_dict.keys():

            print("\n#######################################")
            print(f"    ... Atualizando {filme} ...")
            print("Para atualizar TUDO, digite [T]")
            print("P/ atualizar só uma chave específica, dgt em inglês")
            print("#######################################")
            upd = input("-> ")

            print("|-(se tiver + de 1, separe por vírgula)--")
            print("|")

            if upd.upper()=="T":
                movie = register()

                #Atribuindo novo valor de chave
                new_key = movie['code']
                del films_dict[filme]

                films_dict[new_key] = movie

                # Armazenando no Banco
                arqFilmes = open('database/movies_db.dat', 'wb')
                pickle.dump(films_dict, arqFilmes)
                arqFilmes.close()

            elif upd in films_dict[filme].keys():

                print(f"New {upd}: ", end="")
                if upd!="duration":
                    val = input()
                else:
                    val = int(input())

                films_dict[filme][upd] = val

                if upd=="title":
                    new_key = films_dict[filme]
                    del films_dict[filme]
                    films_dict[val] = new_key

                # Armazenando no Banco
                arqFilmes = open('database/movies_db.dat', 'wb')
                pickle.dump(films_dict, arqFilmes)
                arqFilmes.close()

            else:
                print("Update Cancelado!")
        else:
            print("Update Cancelado! (ou não tem filmes com esse título)")
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
        print("........................")
        opcoes(films_dict)
        print("\n========================")

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
        for fkey in (films_dict):
            print(f"\n\n#### • Filme: {films_dict[fkey]['code']} • ####\n")

            print("GÊNERO(s): \n•", end="")
            for gnr in films_dict[fkey]['genre']:
                print("", gnr, end=" -")
            print()
            print("DIRETOR(es): \n•", end="")
            for dir in films_dict[fkey]['director']:
                print("", dir, end=" -")

            print("\nDATA DE LANÇAMENTO: ", films_dict[fkey]["release"])
            print("CLASSIF. INDICATIVA: ",  films_dict[fkey]["class_ind"])

            hora    = (films_dict[fkey]["duration"])//60
            minutos = (films_dict[fkey]["duration"])%60
            print(f"DURAÇÃO: {hora}h {minutos}min\n--------------------------")

        input("Tecle ENTER para continuar...\n\n")