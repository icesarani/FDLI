def crearMatrizN(filas,columnas): #relleno con numero ingresados por el cliente
    matriz = [] #lista que contiene listas
    for f in range(filas): #armo una fila
        matriz.append([])
        for c in range(columnas): #le agrego las columnas
            num = int(input(f"Ingrese un valor para la columna {c} de la fila {f}: "))
            matriz[f].append(num)
    return matriz

def ordenaSeleccion(lista): #menor a mayor
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
def mostrarMatrizEnc(matriz): #muestro la matriz de forma grafica
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print()
                
def ordenarFilasM(matriz):
    for i in range(len(matriz)):
        ordenaSeleccion(matriz[i])

matriz = crearMatrizN(3,3)
mostrarMatrizEnc(matriz)
print()
ordenarFilasM(matriz)
mostrarMatrizEnc(matriz)
