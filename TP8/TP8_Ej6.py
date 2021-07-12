import random

def crearMatrizA(filas,columnas,a,b): #relleno con numeros random (no olvidar incluir el random)
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            num = random.randint(a,b) #ingresar entre que valores se realizan
            matriz[f].append(num)
    return matriz

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
        
def sumaMatricez(matriz1,matriz2,matriz3): #ingreso matrices a sumar y la m3 es en la que se pasma el resultado
    for f in range(len(matriz1)):
        for c in range(len(matriz1[0])):
            matriz3[f][c] = matriz1[f][c] + matriz2[f][c]

a = int(input("Ingrese desde que valor va a ser el numero aleatorio: "))
b = int(input("Ingrese el valor hasta el que se van a generar num aleatorios: "))
while(a>=b):
    a = int(input("Ingrese desde que valor va a ser el numero aleatorio: "))
    b = int(input("Ingrese el valor hasta el que se van a generar num aleatorios: "))

matriz1 = crearMatrizA(3,3,a,b)
matriz2 = crearMatrizA(3,3,a,b)
matriz3 = crearMatrizC(3,3)

sumaMatricez(matriz1,matriz2,matriz3)
        
mostrarMatrizEnc(matriz1)
print("+")
mostrarMatrizEnc(matriz2)
print("=")
mostrarMatrizEnc(matriz3)
        