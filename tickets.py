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

    ha_filme   = movies.tem_filme(films_dict)
    ha_cliente = clients.tem_client(clients_dict)
    if ha_filme and ha_cliente:
        print("\n=========================")
        print("==        COMPRA       ==")
        print(".........................")
        movies.see_all(films_dict)
        print("-------------------------")

        opt   = input("Qual filme você quer (dgt o CÓDIGO): ").upper()

        # Associar AQUI
        movie = films_dict[opt]

        date  = input("Data da sessão: ")
        time  = input("Hora da sessão: ")
        seat  = input("Qual assento (poltrona): ")
        sess  = input("Qual sessão/sala (Dgt: 1, 2,... n): ")
        price = float(input('(formato "X.XX") Qual o preço do ingresso? R$ '))

        round_price = format(price, ".2f")
        code = seat+"S"+sess

        clients.see_all(clients_dict)
        print("\n[Dgt o CPF] Para qual cliente? ")
        cpf_client    = input(" -> ")

        # Associar AQUI
        client = clients_dict[cpf_client]

        ticket = {
            'code': code.upper(),
            'movie': movie,
            'date': date,
            'time': time,
            'client': client,
            'price': round_price
        }

        tickets_dict[(ticket['code'])] = ticket

        print("  ...Ingresso adquirido com sucesso!...")

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
def delete_ticket(tickets_dict):
    # (verificar se é admin)

    ha_ingresso = tem_ingresso(tickets_dict)
    if (ha_ingresso):
        # Printa as opções de filmes
        print("\n########################")
        see_all(tickets_dict)
        print("Qual ingresso quer deletar ([0] para Cancelar): ")

        code = input("-> ").upper()
        if code=="0":
            print("Cancelado!")
            return
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

    ha_ingresso = tem_ingresso(tickets_dict)
    if (ha_ingresso):
        for chave in tickets_dict.keys():
            print(f"\n====== INGRESSO DE - {tickets_dict[chave]['client']['name']} - ======")
            print(f'Poltrona "{tickets_dict[chave]["code"]}": ')
            print(f"• {tickets_dict[chave]['movie']['title']}")
            print(f"• {tickets_dict[chave]['date']} às {tickets_dict[chave]['time']}")
            print(f"(Custo): R$ {tickets_dict[chave]['price']}")
            print("-----------------------\n\n")
            input("Tecle ENTER para continuar...\n\n")
