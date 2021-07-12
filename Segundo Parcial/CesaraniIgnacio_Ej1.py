#import random (para las pruebas)

def mostrarMatrizEnc(matriz):
    ''' Muestro la matriz de forma grafica '''
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print()
        
def ordenaMatriz(lista,lista2):
    ''' Ordeno la matriz de menor a mayor '''
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
                aux2 = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux2

def ingresarYvalidar(y):
    ''' Ingresa un valor del codigo que tiene que ser mayor a y con excepcion en -1 para finalizar el codigo.'''
    cod = int(input("Ingrese el codigo del producto(Ingrese -1 para finalizar.): ")) # random.randint(1000,1020) para pruebas
    while(cod<y and cod>-1)or(cod<-1):
        cod = int(input("El valor ingresado para el codigo es invalido, ingrese un codigo correcto: ")) # random.randint(1000,1020) para pruebas
    return cod

def encontrarRepetidos(lista,valor):
    ''' Busca un valor repetido en una lista y devuelve su posicion, si no lo encuentra devuelve -1 '''
    pos = -1
    for i in range(len(lista)):
        if(lista[i]==valor):
            pos = i
    return pos

def limpiarStockN(matriz):
    ''' Ingreso una matriz y segun su fila 2 limpio de columnas con valores negativos '''
    for i in range(len(matriz[1]),0,-1):
        if(matriz[1][i-1]<0):
            matriz[0].pop(i-1)
            matriz[1].pop(i-1)
            
def matrizMenorN(matriz1,matriz2, n):
    ''' Genero una nueva matriz con los productos que contienen un stock menor a N '''
    for i in range(len(matriz1[1])):
        if(matriz1[1][i]<=n):
            matriz2[0].append(matriz1[0][i])
            matriz2[1].append(matriz1[1][i])


''' Sistemas que registra codigo y stock de un producto, si el stock es negativo
    se elimina de la lista junto con su codigo. Luego se ordena la matriz por menor a mayor
    de stock y por ultimo se genera una nueva matriz con los stocks que no sobre pasen el valor
    N ingresado por el cliente. '''

y = 999 #Variable que determina el menor numero aceptable en los codigos

autosCS = [[],[]] #creo la matriz con codigos en la primer fila y stock en la segunda

cod = ingresarYvalidar(y) #ingreso el codigo y lo verifico en la funcion
while(cod!=-1): #Si se ingresa -1 se termina la cargada de codigos (en las pruebas usar 1000)
    
    stock = int(input("Ingrese el stock a sumar, si desea restar use los negativos: ")) #random.randint(-40,40) para pruebas
    
    posR = encontrarRepetidos(autosCS[0],cod) #busco si el codigo esta repetido
    if(posR == -1): #si no se encuentra repetido el codigo:
        autosCS[0].append(cod) #agrego el codigo
        autosCS[1].append(stock) #agrego el stock para el codigo
    else: #si esta repetido
        autosCS[1][posR] = autosCS[1][posR] + stock #sumo el stock ingresado para el codigo
        
    cod = ingresarYvalidar(y) #ingreso un nuevo codigo para que continue el while
    
limpiarStockN(autosCS) #limpio la matriz de autos con stock negativo

ordenaMatriz(autosCS[1],autosCS[0]) #ordeno la matriz de menor a mayor segun su stock

print("El inventario automotriz es el siguiente dividido en filas por codigo de producto y stock: ")
mostrarMatrizEnc(autosCS) #muestro matriz de automoviles

n = int(input("Ingrese que numero de stock no debe superar para mostrarse: "))

matrizMN = [[],[]] #matriz secundario con valores menores o iguales a N

matrizMenorN(autosCS,matrizMN,n)

print("Los productos que cumplen con el stock no mayor a",n,"son los siguientes: ")
mostrarMatrizEnc(matrizMN)



    
    
    
    
