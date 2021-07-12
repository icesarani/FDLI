import random

def ingresarNum(): #crear lista con numeros ingresados entre dos paramentros
    lista = []
    a = int(input("Ingresar el primer numero de parametro: "))
    b = int(input("Ingresar el segundo numero de parametro: "))

    num = int(input("Ingrese el numero que desea sumar a la lista, para terminar el proceso ingresar -1. "))
    while(num!=-1):
        if (num < a or num > b):
            num = int(input("ERROR Ingrese un numero valido dentro del rango de a y b: "))
        lista.append(num)
        num = int(input("Ingrese el numero que desea sumar a la lista, para terminar el proceso ingresar -1. "))

    return lista

def crearLista(desde,hasta): #crear una lista con numeros random ingresando cantidad
    n = int(input("Ingrese la cantidad de numeros que desea que se agreguen a la lista: "))
    lista = []
    for i in range(n):
        num = random.randint(desde,hasta)
        lista.append(num)
    return lista

def encontrarValores(lista, valor): #encuentra un valor en una lista y devuelve lista con posiciones
    pos = []
    for i in range(0,len(lista),1):
        if(lista[i]==valor):
            pos.append(i+1)
    if(lista==[]):
        pos = -1
    return pos

def encontrarValor(lista, valor): #encuentra un valor y devuelve su primera posicion
    pos = -1
    i = 0
    j = len(lista)
    while(i<j and pos==-1):
        if(lista[i]==valor):
            pos = i+1
        i = i + 1
    return pos

