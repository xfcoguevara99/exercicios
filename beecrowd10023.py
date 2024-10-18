#coding: utf-8
import math as math
def obtencaoDados(i):
    #dados_por_inmovel = []
    dados_do_inmovel = input(f"Ingresse o numero de pessoas seguido do consumo total do inmovel {i+1}: ").split()
    print(dados_do_inmovel)
    dados_do_inmovel[0],dados_do_inmovel[1] = dados_do_inmovel[1],dados_do_inmovel[0]
    #numero_pessoas_no_inmovel = input(f"Entre com o numero de pessoas no inmovel {i+1}: ")
    #consumo_no_inmovel = input(f"Informe o consumo no inmovel {i+1}: ")
    #almacenamentoDados(dados_do_inmovel,dados_por_inmovel)
    return dados_do_inmovel

def almacenamentoDados(dado,memoria):
    valor = dado.replace(" ","-")
    memoria.append(valor)
    return

def consumoPessoaNoInmovel(dados):
    return math.floor(int(dados[0])/int(dados[1]))

def CalculoModificacaoDosDadosCidade(lista_com_dados):
    numero_cidades = len(lista_com_dados)
    for i in range(numero_cidades):
        numero_de_inmoveis_na_cidade = len(lista_com_dados[i])
        for j in range(numero_de_inmoveis_na_cidade):
            lista_com_dados[i][j][0] = consumoPessoaNoInmovel(lista_com_dados[i][j])





if __name__ == "__main__":
    numero_inmoveis_na_cidade = int(input("Ingresse o numero de inmoveis na cidade: "))
    dados_cidades = []
    while numero_inmoveis_na_cidade !=0:
        dados_inmoveis_por_cidade = []
        for i in range(numero_inmoveis_na_cidade): 
            dados_recibidos_inmovel = obtencaoDados(i)
            dados_inmoveis_por_cidade.append(dados_recibidos_inmovel)
        dados_cidades.append(dados_inmoveis_por_cidade)
        numero_inmoveis_na_cidade = int(input("Ingresse o numero de inmoveis na cidade: "))
    print(dados_cidades)
    
    CalculoModificacaoDosDadosCidade(dados_cidades)
    print(dados_cidades)

    numero_da_cidade = len(dados_cidades) 
    for i in range(numero_da_cidade):
        num = 0
        for j in range(len(dados_cidades[i])):
            pass
            