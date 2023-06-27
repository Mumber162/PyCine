# CADASTRAR
def register(films_dict):
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print("|")
    print("\n--(se tiver + de 1, separe por vírgula)--")
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

# BUSCAR

# ATUALIZAR

# REMOVER

# VER
def see_all(films_dict):
    for i in range(len(films_dict)):
        print("\n-----=== - X FILME %d X - ===---------" % (int(i)+1))
        print()
        print("TÍTULO: ",              films_dict[i]["title"])
        print("GÊNERO(s): ",           films_dict[i]["genre"])
        print("DIRETOR(es): ",         films_dict[i]["director"])
        print("DATA DE LANÇAMENTO: ",  films_dict[i]["release"])
        print("CLASSIF. INDICATIVA: ", films_dict[i]["class_ind"])
        print("DURAÇÃO: ",             films_dict[i]["duration"], "(min)")
        print("- - - - - =-= - - - =-= - - - - -")