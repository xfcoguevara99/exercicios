#coding: utf-8


if __name__ == "__main__":
    numero_inmoveis_na_cidade = int(input())
    numero_cidade = 1
    while numero_inmoveis_na_cidade:
        lista_numero_pessoa = []
        lista_consumo_medio_por_pessoa = []
        soma_consumo_dos_inmoveis = 0
        soma_total_pessoas = 0
        for i in range(numero_inmoveis_na_cidade):
            entrada = input().split(" ")
            numero_pessoa = int(entrada[0])
            consumo_do_inmovel = int(entrada[1])
            consumo_medio = int(consumo_do_inmovel/numero_pessoa)
            if consumo_medio not in lista_consumo_medio_por_pessoa:
                lista_consumo_medio_por_pessoa.append(consumo_medio)
                lista_numero_pessoa.append(numero_pessoa)
            else:
                lista_numero_pessoa[lista_consumo_medio_por_pessoa.index(consumo_medio)] += numero_pessoa
            soma_consumo_dos_inmoveis += consumo_do_inmovel
            soma_total_pessoas += numero_pessoa
        print(f'Cidade# {numero_cidade}:')
        for i in range(len(lista_consumo_medio_por_pessoa)):
            consumo_minimo_na_cidade = min(lista_consumo_medio_por_pessoa)
            indice_do_consumo_minimo = lista_consumo_medio_por_pessoa.index(consumo_minimo_na_cidade)
            print(f"{lista_numero_pessoa[indice_do_consumo_minimo]}-{consumo_minimo_na_cidade}",end = " ")
            lista_numero_pessoa.pop(indice_do_consumo_minimo)
            lista_consumo_medio_por_pessoa.pop(indice_do_consumo_minimo)
        print("\nConsumo medio: {:.2f} m3.".format(int(soma_consumo_dos_inmoveis/soma_total_pessoas*100)/100))
        numero_inmoveis_na_cidade = int(input())
        if numero_inmoveis_na_cidade:
            print("\n")


"""numero_cidade = 1              
while True:
    numero_inmoveis_na_cidade = int(input())
    if numero_inmoveis_na_cidade == 0:
        break

    lista_consumos = {}  # Dicionário para armazenar o consumo médio e o número total de pessoas
    soma_consumo_dos_inmoveis = 0
    soma_total_pessoas = 0

    for _ in range(numero_inmoveis_na_cidade):
        numero_pessoa, consumo_do_inmovel = map(int, input().split())
        consumo_medio = consumo_do_inmovel / numero_pessoa

        # Acumulando o número de pessoas para cada consumo médio
        if consumo_medio in lista_consumos:
            lista_consumos[consumo_medio] += numero_pessoa
        else:
            lista_consumos[consumo_medio] = numero_pessoa

        soma_consumo_dos_inmoveis += consumo_do_inmovel
        soma_total_pessoas += numero_pessoa

    # Imprimindo o resultado da cidade
    print(f'Cidade# {numero_cidade}:')
    
    # Ordenando os consumos por consumo médio (menor para maior)
    for consumo in sorted(lista_consumos.keys()):
        print(f"{lista_consumos[consumo]}-{int(consumo)}", end=" ")
    
    # Cálculo do consumo médio geral
    consumo_medio_cidade = soma_consumo_dos_inmoveis / soma_total_pessoas
    print(f"\nConsumo medio: {consumo_medio_cidade:.2f} m3.")

    numero_cidade += 1
    print()"""