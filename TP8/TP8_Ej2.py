import random

def crearMatrizA(filas,columnas): #relleno con numeros random (no olvidar incluir el random)
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            num = random.randint(0,100) #ingresar entre que valores se realizan
            matriz[f].append(num)
    return matriz

def mostrarMatrizEnc(matriz): #muestro la matriz de forma grafica
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print()

filas = int(input("Ingrese la cantidad de filas que desea que contenga la matriz: "))
while(filas<1):
    filas = int(input("Ingrese un valor positivo para las filas: "))
columnas = int(input("Ingrese la cantidad de columnas que desea que tenga su matriz: "))
while(columnas!=filas):
    columnas = int(input("La cantidad de columnas y filas deben ser la misma: "))
matriz = crearMatrizA(filas, columnas)

mostrarMatrizEnc(matriz)

suma = 0
for f in range(0,len(matriz),1):
    c = 0
    for c in range(len(matriz[0])-f):
        suma = suma + matriz[f][c]
        c = c + 1

print(suma)
        