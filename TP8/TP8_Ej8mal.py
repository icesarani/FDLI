import random

def crearMatrizC(filas,columnas): #relleno con ceros (en blanco)
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            matriz[f].append(0)
    return matriz

def mostrarMatrizEnc(matriz): #muestro la matriz de forma grafica
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print()
        
def sumX2Col(matriz):
    num=0
    j = 1
    for i in range(len(matriz[0]),1,-2):
        for c in range(len(matriz[0])):
            for f in range(0,2,1):
                num=num+1
                matriz[f*j][c] = num
        j=j+1

        

matriz = crearMatrizC(4,4)

mostrarMatrizEnc(matriz)

sumX2Col(matriz)

mostrarMatrizEnc(matriz)