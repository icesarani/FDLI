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

def ordenaSeleccion(lista,listaa): #menor a mayor
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
                aux2 = listaa[i]
                listaa[i] = listaa[j]
                listaa[j] = aux2

def juego():
    num = random.randint(1000,9999)
    enc = False
    intentos = 0
    while(enc==False):
        intento = int(input("Ingrese el numero que piensa que es: (Puede terminar el juego ingresando -1)"))
        if(intento<num):
            print("El numero ingresado es menor al numero generado por el programa.")
            intentos=intentos+1
        elif(intento>num):
            print("El numero ingresado es mayor al numero generado por el programa.")
            intentos=intentos+1
        elif(intento==num):
            print("Felicitaciones! Encontro el numero generado, uso",intentos,"intentos.")
            enc = True
    return intentos

def mostrarMatrizEnc(matriz): #muestro la matriz de forma grafica
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f][c], end=" ")
        print()

def agregarMenorIntentos(matriz, intentos, dni):
    matriz[0][4] = matriz[0][3]
    matriz[0][3] = matriz[0][2]
    matriz[0][2] = matriz[0][1]
    matriz[0][1] = matriz[0][0]
    matriz[0][0] = intentos
    
    matriz[1][4] = matriz[1][3]
    matriz[1][3] = matriz[1][2]
    matriz[1][2] = matriz[1][1]
    matriz[1][1] = matriz[1][0]
    matriz[1][0] = dni
    

def puntuacion(matriz, intentos):
    ordenaSeleccion(matriz[0],matriz[1])
    if(intentos<matriz[0][0]):
        dni = int(input("Ingrese su dni para guardar su puntuacion: "))
        agregarMenorIntentos(matriz, intentos, dni)
    print("Las mejores 5 puntuaciones tienen los siguientes numeros de intentos y su dni es: ")
    mostrarMatrizEnc(matriz)
    
mejoresC = crearMatrizN(2,5)
intentos = juego()
puntuacion(mejoresC, intentos)
volverJugar = False
j = int(input("Si desea volver a jugar ingrese 0, si desea terminar el juego ingrese 1:  "))
if(j==0):
    volverJugar = True
elif(j==1):
    volverJugar = False

while(volverJugar==True):
    intentos = juego()
    puntuacion(mejoresC, intentos)
    
    j = int(input("Si desea volver a jugar ingrese 0, si desea terminar el juego ingrese 1:  "))
    if(j==0):
        volverJugar = True
    elif(j==1):
        volverJugar = False
