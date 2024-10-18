#coding: utf-8
def obtencaoDados(i):
    #dados_por_inmovel = []
    dados_do_inmovel = input(f"Ingresse o numero de pessoas seguido do consumo total do inmovel {i}: ").replace(" ","-")
    #numero_pessoas_no_inmovel = input(f"Entre com o numero de pessoas no inmovel {i+1}: ")
    #consumo_no_inmovel = input(f"Informe o consumo no inmovel {i+1}: ")
    #almacenamentoDados(dados_do_inmovel,dados_por_inmovel)
    return dados_do_inmovel

def almacenamentoDados(dado,memoria):
    valor = dado.replace(" ","-")
    memoria.append(valor)
    return

def consumoPessoaNoInmovel(dados):
    return int(int(dados[1])/int(dados[0]))

def CalculoModificacaoDosDadosCidade(lista_com_dados):
    numero_cidades = len(lista_com_dados)
    for i in range(numero_cidades):
        numero_de_inmoveis_na_cidade = len(lista_com_dados[i])
        for j in range(numero_de_inmoveis_na_cidade):
            dados = lista_com_dados[i][j].split("-")
            lista_com_dados[i][j] = dados[0] + "-" + str(consumoPessoaNoInmovel(dados))





if __name__ == "__main__":
    numero_inmoveis_na_cidade = int(input("Ingresse o numero de inmoveis na cidade: "))
    dados_cidade = []
    while numero_inmoveis_na_cidade !=0:
        dados_inmoveis_por_cidade = []
        for i in range(numero_inmoveis_na_cidade): 
            dados_recibidos_inmovel = obtencaoDados(i)
            dados_inmoveis_por_cidade.append(dados_recibidos_inmovel)
        dados_cidade.append(dados_inmoveis_por_cidade)
        numero_inmoveis_na_cidade = int(input("Ingresse o numero de inmoveis na cidade: "))
    print(dados_cidade)
    
    CalculoModificacaoDosDadosCidade(dados_cidade)
    print(dados_cidade)

    numero_da_cidade = len(dados_cidade) 
    for i in range(1,numero_da_cidade+1):
        num = 0
        for j in range(len(dados_cidade[i])):
            
    
        


    