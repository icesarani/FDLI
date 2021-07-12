def ordenaSeleccion(lista,lista2): #menor a mayor
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
                aux2 = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux2
                
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
                

numUni = []
supMC = []
sumaExp = 0
valorFijo = int(input("Ingese el valor fijo por metro cuadrado: "))
for i in range(0,20,1):
    ordenaSeleccion(numUni,supMC)
    numU = int(input("Ingresar la numeracion de la unidad: "))
    bool = busquedaBinaria(numUni, numU)
    while(bool == True):
        numU = int(input("Ingresar la numeracion de la unidad: "))
        bool = busquedaBinaria(numUni, numU)
    numUni.append(numU)
    mCUni = int(input("Ingrese los metros cuadrados por unidad: "))
    while(mCUni<1):
        mCUni = int(input("El valor ingresado para la superficie es invalida, ingrese un valor permitido: "))
    supMC.append(mCUni)
    sumaExp = sumaExp + (mCUni*valorFijo)
promExp = sumaExp/20
ordenaSeleccion(supMC, numUni)
print("El promedio de expensas es",promExp)
print(supMC, numUni)