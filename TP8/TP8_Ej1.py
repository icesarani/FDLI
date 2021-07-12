import random

def crearMatrizA(filas,columnas): #relleno con numeros random (no olvidar incluir el random)
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            num = random.randint(1,10) #ingresar entre que valores se realizan
            matriz[f].append(num)
    return matriz

def mostrarMatrizEnc(matriz): #muestro la matriz de forma grafica
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print()

matriz = crearMatrizA(3,4)
mostrarMatrizEnc(matriz)