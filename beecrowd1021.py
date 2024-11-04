notas = [100,50,20,10,5,2]
moedas = [1,0.50,0.25,0.10,0.05,0.01]
valor = float(input())
n = 0
print("NOTAS:")
for i in notas:
    quantidadeDeNotasOuMoedas = valor // i
    print(f"{int(quantidadeDeNotasOuMoedas)} nota(s) de R$ {i:.2f}")
    valor = round(valor % i,2)

print("MOEDAS:")
for i in moedas:
    if i != 0.01:
        quantidadeDeNotasOuMoedas = valor // i
    else:
        quantidadeDeNotasOuMoedas = valor / i
    print(f"{int(quantidadeDeNotasOuMoedas)} moeda(s) de R$ {i:.2f}")
    valor = round(valor % i,2)
