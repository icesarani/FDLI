def ingresarNum():
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

def capicua(lista):
    capicuaa = True
    cont = 0
    i = int(len(lista))-1
    while(cont<=(len(lista)//2) and capicuaa==True):
        c = i-cont
        a = lista[cont]
        b = lista[c]
        if(a!=b):
            capicuaa = False
        cont=cont+1
    return capicuaa
    
lista = ingresarNum()
print("La longitud de la lista es",len(lista))
escap = capicua(lista)
if(escap==True):
    print("Es capicua")
else:
    print("Es no es capicua")