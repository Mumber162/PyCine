#--------------------------------
import users
#================================

def tem_filme(films_dict):
    if not films_dict:
        print(" _____________________________ ")
        print("|                             |")
        print("|  NÃO HÁ FILMES CADASTRADOS  |")
        print("|                             |")
        print(" =---------------------------= ")

        input("Tecle ENTER para continuar...\n\n")

        return False
    else:
        return True

""""""
# CADASTRAR Filmes
""""""
def register(films_dict):
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
        "title":     title,
        "genre":     genres,
        "director":  directors,
        "release":   release,
        "class_ind": class_ind,
        "duration":  duration
        }

    films_dict.append(movie)


""""""
# BUSCAR
""""""
def search(films_dict):

    ha_filme = tem_filme(films_dict)
    if (ha_filme):
        print("======================================")
        name_search = input("Digite o nome do filme: ").lower()

        print("###############=- RESULTADO(s) -=###############\n")
        films_buscados = []
        for i in range(len(films_dict)):
            name_movie = films_dict[i]["title"].lower()

            if name_search==name_movie:
                films_buscados.append(i)

        if len(films_buscados)==0:
            print("    Não há filmes cadastrados com esse título\n")
            print("################################################\n\n\n")
        else:
            for j in range(len(films_buscados)):
                print(f"{int(j)+1}: {films_dict[(films_buscados[j])]['title']} ({films_dict[(films_buscados[j])]['release']})")


""""""
# ATUALIZAR
""""""
def update_film(films_dict):
    # if (users.verifica_cargo())

    ha_filme = tem_filme(films_dict)
    if (ha_filme):
        # Printa as opções de filmes
        for i in range(len(films_dict)):
            print(f"{int(i)+1}. {films_dict[i]['title']} ({films_dict[i]['release']})")

        print("\n##################################")
        filme = int(input("[Dgt o nº] Qual filme atualizar? "))

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

        # Atualização
        films_dict[filme-1]["title"]     = title
        films_dict[filme-1]["genre"]     = genres
        films_dict[filme-1]["director"]  = directors
        films_dict[filme-1]["release"]   = release
        films_dict[filme-1]["class_ind"] = class_ind
        films_dict[filme-1]["duration"]  = duration


""""""
# REMOVER
""""""
def delete_film(films_dict):
    # (verificar se é admin)

    ha_filme = tem_filme(films_dict)
    if (ha_filme):
        # Printa as opções de filmes
        print("\n##############################")
        print("Qual filme quer deletar:")
        print("##############################\n")
        for i in range(len(films_dict)):
            print(f"{int(i)+1}. {films_dict[i]['title']} ({films_dict[i]['release']})")
        print("\n==============================")

        option = (int(input("-> ")))-1  
        del films_dict[option]

        print("= Filme Deletado com Sucesso!")
        input("Tecle ENTER para continuar...\n\n")


""""""
# VER
""""""
def see_all(films_dict):

    ha_filme = tem_filme(films_dict)
    if (ha_filme):
        for film in (films_dict):
            print("\n########## • FILME • ##########")
            print()
            print("TÍTULO: ", film["title"])

            print("GÊNERO(s): \n•", end="")
            for gnr in film["genre"]:
                print("", gnr, end=" -")
            print()
            print("DIRETOR(es): \n•", end="")
            for dir in film["director"]:
                print("", dir, end=" -")
            print()

            print("DATA DE LANÇAMENTO: ",  film["release"])
            print("CLASSIF. INDICATIVA: ", film["class_ind"])

            hora    = (film["duration"])//60
            minutos = (film["duration"])%60
            print(f"DURAÇÃO: {hora}h {minutos}min")

        input("Tecle ENTER para continuar...\n\n")
    