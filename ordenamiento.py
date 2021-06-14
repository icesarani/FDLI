def ordenaSeleccion(lista): #menor a mayor
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
def ordenaSeleccionI(lista): #mayor a menor
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i] < lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def metodoBurbuja(lista): #menor a mayor
    for recorrido  in range(1,len(lista)):
        for i in range(0,len(lista)-recorrido):
            if(lista[i]>lista[i+1]):
                aux = lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                
def busquedaBinaria(lista, valor): #debe estar ordenada de menor a mayo // devuelve bool si esta el valor
    izq = 0
    der = len(lista)-1
    enc = False
    while(izq<=der and enc==False):
        centro=(izq+der)//2
        if(lista[centro]==valor):
            enc=True
        elif(lista[centro]<valor):
            izq= centro+1
        else:
            der = centro-1
    return enc

def busquedaBinaria(lista, valor): #debe estar ordenada de menor a mayo // devuelve pos del valor
    izq = 0
    der = len(lista)-1
    pos = -1
    while(izq<=der and pos==-1):
        centro=(izq+der)//2
        if(lista[centro]==valor):
            pos = centro
        elif(lista[centro]<valor):
            izq= centro+1
        else:
            der = centro-1
    return pos
    
lista=[1,7,5,2,6]
print(lista)
ordenaSeleccion(lista)
print(lista)