import random

def crearMatrizC(filas,columnas): #relleno con ceros (en blanco)
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            matriz[f].append(0)
    return matriz

def crearMatrizN(filas,columnas): #relleno con numero ingresados por el cliente
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            num = int(input(f"Ingrese un valor para la columna {c} de la fila {f}: "))
            matriz[f].append(num)
    return matriz

def crearMatrizA(filas,columnas): #relleno con numeros random (no olvidar incluir el random)
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            num = random.randint(0,100) #ingresar entre que valores se realizan
            matriz[f].append(num)
    return matriz

def mostrarMatriz(matriz): #mostrar la matriz
    filas = len(matriz)
    columnas = len(matriz[0])
    print(f"Tiene {filas} filas y {columnas} columnas.")
    
def mostrarMatrizEnc(matriz): #muestro la matriz de forma grafica
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print()

def sumarFilas(matriz): #sumo las filas de una matriz
    lstSumas = []
    for f in range(len(matriz)):
        suma = 0
        for c in range(len(matriz[f])):
            suma = suma+matriz[f][c]
        lstSumas.append(suma) #guardo la suma de la fila f en la lista lstSumas
    return lstSumas

def sumarColumnas(matriz): #sumo las columnas de una matriz
    lstSumas = []
    for c in range(len(matriz[0])):
        suma = 0
        for f in range(len(matriz)):
            suma = suma + matriz[f][c]
        lstSumas.append(suma)
    return lstSumas

def sumaDiagonal(matriz): #suma de la diagonla principal de una matriz
    sumaDiagonal1=0
    for i in range(len(matriz)):
        sumaDiagonal1 = sumaDiagonal1+matriz[i][i]
    return sumaDiagonal1

def sumaMatricez(matriz1,matriz2,matriz3): #ingreso matrices a sumar y la m3 es en la que se pasma el resultado
    for f in range(len(matriz1)):
        for c in range(len(matriz1[0])):
            matriz3[f][c] = matriz1[f][c] + matriz2[f][c]

    
matriz1 = crearMatrizA(3,3)
print(matriz1)
mostrarMatrizEnc(matriz1)