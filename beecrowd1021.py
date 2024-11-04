def scrip1():
    notas = [100,50,20,10,5,2]
    moedas = [1,0.50,0.25,0.10,0.05,0.01]
    resto_da_divisao = 0
    valor = float(input())
    print("NOTAS:")
    for i in notas:
        quantidade_inteira_NotasOuMoedas = valor // i
        resto_da_divisao = round(valor % i,2)
        valor = resto_da_divisao
        print(f"{int(quantidade_inteira_NotasOuMoedas)} nota(s) de R$ {i:.2f}")
    print("MOEDAS:") 
    # Duas opções de fazer o calculo das moedas 
    def moedas_opcao1(valor):
        for i in moedas:
            if i != 0.01:
                quantidade_inteira_NotasOuMoedas = valor // i
            else:
                quantidade_inteira_NotasOuMoedas = valor / i

            resto_da_divisao = round(valor% i,2)
            valor = resto_da_divisao
            print(f"{int(quantidade_inteira_NotasOuMoedas)} moeda(s) de R$ {i:.2f}")
    
    def moedas_opcao2(valor):
        valor = valor * 100
        for i in moedas:
            i *= 100
            quantidade_inteira_NotasOuMoedas = valor // i
            resto_da_divisao = round(valor% i,2)
            valor = resto_da_divisao
            print(f"{int(quantidade_inteira_NotasOuMoedas)} moeda(s) de R$ {i/100:.2f}")
    
    print("Algorismo 1:")
    moedas_opcao1(valor)
    print("Algorismo 2:")
    moedas_opcao2(valor)

def scrip2():
    lista_flotante = list(i/100 for i in range(1,20))
    for i in lista_flotante:
        print(f"A divisão inteira de {i} por 0.01 no python é: {int(i//0.01)} ")


if __name__ == "__main__":
    scrip1()
    print("\nCuriosidade da divisão inteira no python \n")
    scrip2()