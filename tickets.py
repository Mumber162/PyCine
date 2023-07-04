#--------------------------------
import pickle
import movies
import clients
#================================

# Verfica se tem ingressos
def tem_ingresso(tickets_dict):
    if not tickets_dict:
        print(" ________________________________ ")
        print("|  NÃO HÁ INGRESSOS CADASTRADOS  |")
        print(" =------------------------------= ")

        input("Tecle ENTER para continuar...\n\n")

        return False
    else:
        return True

""""""
# CADASTRAR/COMPRAR Ingressos
""""""
def buy(clients_dict, films_dict, tickets_dict):

    ha_filme = movies.tem_filme(films_dict)
    if ha_filme:
        print("\n=========================")
        print("==        COMPRA       ==")
        print(".........................")
        movies.see_all(films_dict)
        print("-------------------------")

        opt       = input("Qual filme você quer? ")
        date_time = input("Data/Hora da sessão: ")
        code      = input("Código do ingresso: ")

        clients.see_all(clients_dict)
        client    = input("Para qual cliente? ")

        ticket = {
            'code': code,
            'movie': opt,
            'date_time': date_time,
            'client': client,
        }

        tickets_dict[(ticket['code'])] = ticket

        # Armazenando no Banco
        arqIngressos = open('database/tickets_db.dat', 'wb')
        pickle.dump(tickets_dict, arqIngressos)
        arqIngressos.close()

""""""
# BUSCAR Ingressos
""""""
def search(tickets_dict):
    ha_ingresso = tem_ingresso(tickets_dict)
    if (ha_ingresso):
        print("\n###############################")
        code_search = input("Digite o codigo do ingresso: ")

        print("========- RESULTADO -=======\n")
        if code_search in tickets_dict.keys():
            print(tickets_dict[code_search])

        else:
            print(" Não há ingressos com esse Código\n")
       
        print("################################\n")
        input("Tecle ENTER para continuar...\n\n")


""""""
# REMOVER
""""""
def delete_film(tickets_dict):
    # (verificar se é admin)

    ha_ingresso = ha_ingresso(tickets_dict)
    if (ha_ingresso):
        # Printa as opções de filmes
        print("\n########################")
        print("Qual ingresso quer deletar: ")

        code = input("-> ")
        del tickets_dict[code]

        # Armazenando no Banco
        arqIngressos = open('database/tickets_db.dat', 'wb')
        pickle.dump(tickets_dict, arqIngressos)
        arqIngressos.close()

        print("........................")
        print("= Ingresso Deletado com Sucesso!")
        input("Tecle ENTER para continuar...\n\n")


""""""
# VER
""""""
def see_all(tickets_dict):
    print(tickets_dict)