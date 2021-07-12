import random

def crearMatrizA(filas,columnas): #relleno con numeros random (no olvidar incluir el random)
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            num = random.randint(100,1000) #ingresar entre que valores se realizan
            matriz[f].append(num)
    return matriz

def mostrarMatrizEnc(matriz): #muestro la matriz de forma grafica
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print()

n = int(input("Ingrese la cantidad de filas que contendra la matriz: "))
while(n <= 1):
    n = int(input("Ingrese la cantidad de filas que contendra la matriz: "))
m = int(input("Ingrese la cantidad de columnas que contendra la matriz: "))
while(m <= 1):
    m = int(input("Ingrese la cantidad de filas que contendra la matriz: "))
    
matriz = crearMatrizA(n,m)

mostrarMatrizEnc(matriz)

numM = [0,0,0]

for f in range(len(matriz)):
    for c in range(len(matriz[0])):
        if(matriz[f][c]>numM[0]):
            numM = [matriz[f][c],f+1,c+1]
            

print(f"El numero mayor encontrado fue {numM[0]}, en la fila {numM[1]} y en la columna {numM[2]}")

