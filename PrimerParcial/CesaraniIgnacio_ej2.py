#Desarrollar un programa que ingrese números hasta que la suma supere un valorN positivo también ingresado por teclado.
#Informar:
#La cantidad de veces que un número es igual al primer valor ingresado.
#La suma y cantidad de valores pares ingresados.

#Entradas: Numeros a Sumar, Numero N (tope)
#Salidas: Suma de valores pares, Cantidad de valores Pares, Cantidad de veces que el numero es igual al primero

#Ingreso el numero tope para saber cuando parar
#Validacion del tope positivo
nTope = int(input("Ingrese el numero tope de la suma: "))
while(nTope<1):
    nTope = int(input("El valor ingresado para el tope es invalido ay que es negativo, ingrese un nuevo valor: "))
nSuma = int(input("Ingrese el primer numero: "))

#inicializo una variable para almacenar la suma constante
sumaT = 0

#Almaceno el primer valor ingresado
primerValor = nSuma

#Variable para cantidad de numeros iguales al primero, se inicializa en -1
#ya que el primer valor siempre va a ser igual a si mismo y se sumaria un caso de más
igualPV = -1

#contador de cantidad de valores pares
cantValoresP = 0

#sumatoria de valores pares
sumaValoresP = 0

while(sumaT<nTope):
    
    #almaceno la suma de los numeros
    sumaT=sumaT+nSuma
    
    #si el numero ingresado es igual al primer valor se suma el conteo
    if(primerValor==nSuma):
        igualPV=igualPV+1
    
    #averiguo si el valor ingresado es par y sumo contadores y variables
    if((nSuma%2)==0):
        cantValoresP=cantValoresP+1
        sumaValoresP = sumaValoresP +nSuma
    
    #si la suma es menor o igual al tope sigo pidiendo numeros 
    if(sumaT<nTope):
        nSuma = int(input("Ingrese un nuevo valor para sumar: "))
    
#imprimo las salidas
print("Se ingresaron",igualPV,"veces un numero/s igual/es al primero")
print("Se ingresaron un total de",cantValoresP,"numero/s pares y su sumatoria da",sumaValoresP)


