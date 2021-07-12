import random

def crearMatrizA(filas,columnas,a,b): #relleno con numeros random (no olvidar incluir el random)
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            num = random.randint(a,b) #ingresar entre que valores se realizan
            matriz[f].append(num)
    return matriz

import random

def mostrarMatriz(matriz):
    '''mostrar por pantalla la matriz'''
    
    filas=len(matriz)
    if filas !=0:
        columnas=len(matriz[0])
        
        print("Tiene",filas,"filas y",columnas,"columnas")
        for f in range(filas):
            for c in range(columnas):
                print("%5d" %matriz[f][c], end=" ")
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
            
filas = int(input("Ingrese la cantidad de filas que desea que contenga la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas que desea en la matriz: "))
a = int(input("Ingrese desde que numero quiere los valores al azar: "))
b = int(input("Ingrese hasta que valor desea que se generen los numeros al azar: "))
if(a==b)or(filas<0)or(columnas<0):
    matriz = []
else:
    matriz = crearMatrizA(filas, columnas, a, b)

mostrarMatriz(matriz)

sumaF = sumarFilas(matriz)
sumaC = sumarColumnas(matriz)

print("La suma de las filas es:",sumaF, "y la suma de las columans es", sumaC)
