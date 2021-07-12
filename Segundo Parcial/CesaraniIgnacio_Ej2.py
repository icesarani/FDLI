import random

def abIngresoVeri():
    ''' Se ingresan A y B, luego se verifica que 0 este entre los valores. Retorna A y B. '''
    
    a = int(input("Ingrese el numero desde el que se generaran los valores: "))
    b = int(input("Ingrese el numero hasta el que se generaran los valores: "))
    while a>0 or b<0 or b<a:
        print("Los numeros que contengan entre A y B deben tener 0. Ademas B no puede ser menor a A...")
        a = int(input("Ingrese un numero valido desde el que se generaran los valores: "))
        b = int(input("Ingrese un numero valido hasta el que se generaran los valores: "))
    return a, b

def rellenarLista(a,b,lista):
    ''' Se rellena la lista con valores generados entre A y B al azar.'''
    x = random.randint(a,b)
    while(x!=0):
        lista.append(x)
        x = random.randint(a,b)
    
def cambiarLugar(lista):
    ''' Cambio de lugar los valores y el primero se dezplasa al ultimo lugar. '''
    auxf = lista[0]
    for i in range(len(lista)-1):
        lista[i] = lista[i+1]
    lista[len(lista)-1] = auxf
        
''' Se genera una lista con numeros entre A y B dentro de los cuales se encuentra el 0
    al generar la lista se muestra y despues se invoca una funcion que envia el primer
    valor al final de la lista y desplaza las otras posiciones.'''

lista = [] #creo lista
a, b = abIngresoVeri() #ingreso y verifico valores a y b
rellenarLista(a,b,lista) #relleno la lista con valores random entre a y b
print(lista)
if(lista==[]): #si la lista esta vacia no se invoca la funcion ya que daria error
    print("La lista generada es vacia...")
else:
    cambiarLugar(lista) #cambio de lugar el primero con el ultimo
    print("La lista invertida es: ")
    print(lista)
    

        
