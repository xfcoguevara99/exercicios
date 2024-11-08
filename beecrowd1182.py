import random as random

def criarMatriz():
    matriz = list()
    for i in range(12):
        fila = [round(random.random()+random.random()*13,1) for j in range(12)]
        matriz.append(fila)
    return matriz

def imprimirMatriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j],end=" ")
        print("\n")



if __name__ =="__main__":
    matriz = criarMatriz()
    
    imprimirMatriz(matriz)
