def ordenaSeleccion2(lista, lista2): #menor a mayor
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
                aux2 = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux2
                
def busquedaBinaria(lista, lista2, valor): #debe estar ordenada de menor a mayo // devuelve nota
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
    return lista2[pos]
    

legajos = [] #lista de legajos
notas = [] #lista de notas
alumApro = 0 #q aprobados
alumDes = 0 #q desaprobados
sumaNotas = 0 #suma total de las notas
qNotas = 0 #q de notas ingresadas
legajo = int(input("Ingrese el numero de legajo, para finalizar la carga ingresar -1: ")) #ingreso legajo
while(legajo != -1): #ciclo con fin -1
    nota = int(input("Ingrese la nota del examen: ")) #ingreso nota
    while(nota<1 or nota>10): #validacion
        nota = int(input("El valor ingresado es incorrecto, ingrese uno valido: "))
    sumaNotas = sumaNotas + nota #suma de todas las notas 
    if(nota>=4): #cuento aprobados
        alumApro = alumApro + 1
    else: #cuento desaprobados
        alumDes = alumDes + 1
    qNotas = qNotas + 1 #cantidad de notas/legajos ingresados
    
    legajos.append(legajo)
    notas.append(nota)
    
    legajo = int(input("Ingrese un nuevo legajo: ")) #vuelvo a ingresar un legajo para seguir con el ciclo

promNotas = sumaNotas/qNotas #calculo prom de notas
legajosSuperan = [] 
for i in range(0,len(notas)): #ciclo que pasa por todas las notas
    if(notas[i]>promNotas): #si la nota es mayor al promedio se suma el legajo a la lista
        legajosSuperan.append(legajos[i])

print("Desaprobaron",alumDes,"alumno/s y aprobaron",alumApro)
print("Los legajos que superaron el promedio fueron",legajosSuperan)

print("Legajos y notas desordenados")
print(legajos)
print(notas)

ordenaSeleccion2(legajos,notas)

print("Legajos y notas ordenados")
print(legajos)
print(notas)

legajoBusq = int(input("Ingrese el legajo que desea encontrar: "))
notaEncontrada = busquedaBinaria(legajos, notas, legajoBusq)
if(notaEncontrada == -1):
    print("El legajo no se fue encontrado.")
else:
    print("La nota del legajo",legajoBusq,"es",notaEncontrada)
