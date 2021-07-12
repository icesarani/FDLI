import random

def crearLista(desde,hasta):
    n = int(input("Ingrese la cantidad de numeros que desea que se agreguen a la lista: "))
    lista = []
    for i in range(n):
        num = random.randint(desde,hasta)
        lista.append(num)
    return lista

def crearListaSumas(lista1,lista2):
    lista3 = []
    for i in range(len(lista1)):
        num = lista1[i] + lista2[i]
        lista3.append(num)
    return lista3

lista1 = crearLista(1,10)
print(lista1)
lista2 = crearLista(1,10)
print(lista2)
lista3 = crearListaSumas(lista1,lista2)
print(lista3)