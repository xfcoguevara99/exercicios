#coding: utf-8


if __name__ == "__main__":
    numero_inmoveis_na_cidade = int(input())
    numero_cidade = 1
    while numero_inmoveis_na_cidade:
        lista_numero_pessoa = []
        lista_consumo_medio_por_pessoa_no_inmovel = []
        soma_consumo_dos_inmoveis = 0
        soma_total_pessoas = 0
        for i in range(numero_inmoveis_na_cidade):
            entrada = list(map(int,input().split(" "))) #Entrada de dois valores separados por um whitespace ex: 3 50
            numero_pessoa = entrada[0]
            consumo_do_inmovel = entrada[1]
            consumo_medio = int(consumo_do_inmovel/numero_pessoa)
            if consumo_medio not in lista_consumo_medio_por_pessoa_no_inmovel:
                lista_consumo_medio_por_pessoa_no_inmovel.append(consumo_medio)
                lista_numero_pessoa.append(numero_pessoa)
            else:
                lista_numero_pessoa[lista_consumo_medio_por_pessoa_no_inmovel.index(consumo_medio)] += numero_pessoa
            soma_consumo_dos_inmoveis += consumo_do_inmovel
            soma_total_pessoas += numero_pessoa

        print("Cidade# {}:".format(numero_cidade))
        for i in range(len(lista_consumo_medio_por_pessoa_no_inmovel)):
            consumo_minimo_na_cidade = min(lista_consumo_medio_por_pessoa_no_inmovel)
            indice_do_consumo_minimo = lista_consumo_medio_por_pessoa_no_inmovel.index(consumo_minimo_na_cidade)
            print("{}-{}".format(lista_numero_pessoa[indice_do_consumo_minimo],consumo_minimo_na_cidade),end = " ")
            del(lista_numero_pessoa[indice_do_consumo_minimo])
            del(lista_consumo_medio_por_pessoa_no_inmovel[indice_do_consumo_minimo])
        print("\nConsumo medio: {:.2f} m3.".format(int(soma_consumo_dos_inmoveis/soma_total_pessoas*100)/100))
        numero_inmoveis_na_cidade = int(input())
        if numero_inmoveis_na_cidade:
            print("\n")
