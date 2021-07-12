import random

def crearLista(desde,hasta):
    n = int(input("Ingrese la cantidad de numeros que desea que se agreguen a la lista: "))
    lista = []
    for i in range(n):
        num = random.randint(desde,hasta)
        lista.append(num)
    return lista

def numMenor(lista):
    posMenor = []
    menor = 101
    cont = 0
    while(lista[cont]!=0) and cont<=len(lista):
        if(menor==lista[cont]):
            posMenor.append(cont)
        if(lista[cont]<menor):
            menor = lista[cont]
            posMenor.append(cont)
        cont=cont+1
    return menor, posMenor

lista = crearLista(0,100)
menor, possMenores = numMenor(lista)
if(menor==0):
    print("No hubo numero menor, el primer numero ingresado fue 0")
else:
    print(f"El numero menor fue {menor} y las posiciones donde aparecion fueron {possMenores}")