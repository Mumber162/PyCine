def register(films_dict):
    print("\n--(se tiver mais de um, separe por vírgula)--")
    print("|                                           | ")
    title     = input("| TÍTULO do filme: "           )
    genre     = input("| GÊNERO(s): "             )
    director  = input("| DIRETOR(es):"          )
    release   = input("| DATA de Lançamento: "    )
    class_ind = input("| Classificação Indicativa: ")
    duration  = input("| Duração (em min): ")

    genres = genre.split(", ")

    movie = {
        "title": title,
        "genre": genre,
        }

    films_dict.append(movie)