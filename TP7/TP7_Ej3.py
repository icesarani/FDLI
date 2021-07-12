import random

def crearLista(desde,hasta):
    n = int(input("Ingrese la cantidad de numeros que desea que se agreguen a la lista: "))
    lista = []
    for i in range(n):
        num = random.randint(desde,hasta)
        lista.append(num)
    return lista

def sumaLista(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma

lista1 = crearLista(1,10)
sumar = sumaLista(lista1)
print(sumar)