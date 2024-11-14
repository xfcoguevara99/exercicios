#coding: utf-8

def deleteNone(lista1,lista2):
    for i in range(len(lista1)-1,-1,-1):
        if lista1[i] ==None:
            del lista1[i]
            del lista2[i]

if __name__ == "__main__":
    numero_inmoveis_na_cidade = int(input())
    numero_cidade = 1
    while numero_inmoveis_na_cidade:
        lista_numero_pessoa = [None]*201
        lista_consumo_medio_por_pessoa_no_inmovel = [None]*201
        soma_consumo_dos_inmoveis = 0
        soma_total_pessoas = 0
        maior_consumo = 0
        menor_consumo = 199
        for i in range(numero_inmoveis_na_cidade):
            entrada = list(map(int,input().split(" "))) #Entrada de dois valores separados por um whitespace ex: 3 50
            numero_pessoa = entrada[0]
            consumo_do_inmovel = entrada[1]
            consumo_medio = int(consumo_do_inmovel/numero_pessoa)
            if consumo_medio>maior_consumo:
                maior_consumo = consumo_medio
            if menor_consumo > consumo_medio:
                menor_consumo = consumo_medio
            if consumo_medio not in lista_consumo_medio_por_pessoa_no_inmovel:
                lista_consumo_medio_por_pessoa_no_inmovel[consumo_medio] = consumo_medio
                lista_numero_pessoa[consumo_medio] = numero_pessoa
            else:
                lista_numero_pessoa[consumo_medio] += numero_pessoa
            soma_consumo_dos_inmoveis += consumo_do_inmovel
            soma_total_pessoas += numero_pessoa
        lista_consumo_medio_por_pessoa_no_inmovel = lista_consumo_medio_por_pessoa_no_inmovel[menor_consumo:maior_consumo+1]
        lista_numero_pessoa = lista_numero_pessoa[menor_consumo:maior_consumo+1]
        deleteNone(lista_consumo_medio_por_pessoa_no_inmovel,lista_numero_pessoa)
        print("Cidade# {}:".format(numero_cidade))
        for i in range(len(lista_consumo_medio_por_pessoa_no_inmovel)):
            print("{}-{}".format(lista_numero_pessoa[i],lista_consumo_medio_por_pessoa_no_inmovel[i]),end = " ")
        print("\nConsumo medio: {:.2f} m3.".format(int(soma_consumo_dos_inmoveis/soma_total_pessoas*100)/100))
        numero_inmoveis_na_cidade = int(input())
        if numero_inmoveis_na_cidade:
            print("\n")
        numero_cidade +=1
