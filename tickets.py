def register(tickets_dict):
    print("\n--(se tiver mais de um, separe por vírgula)--")
    print("|                                           | ")
    title     = input("| NÚMERO do ingresso: ")
    # genre     = input("| GÊNERO(s): "             )
    # director  = input("| DIRETOR(es):"          )
    # release   = input("| DATA de Lançamento: "    )
    # class_ind = input("| Classificação Indicativa: ")
    # duration  = input("| Duração (em min): ")

    # genres = genre.split(", ")
    # directors = director.split(", ")

    ticket = {
        # "title":     title,
        # "genre":     genres,
        # "director":  directors,
        # "release":   release,
        # "class_ind": class_ind,
        # "duration":  duration
        }

    tickets_dict.append(ticket)