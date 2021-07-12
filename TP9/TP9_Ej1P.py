

legajos = []
notas = []

legajo = int(input("Ingrese el numero de legajo del alumno, para terminar el programa ingresar -1: "))
while(legajo != -1):
    legajos.append(legajo)
    nota = int(input("Ingrese la nota del alumno: "))
    while(nota<1 or nota>10):
        nota = int(input("El valor ingresado para la nota del alumno es invalida, ingrese una nota valida: "))
    notas.append(nota)
    legajo = int(input("Ingrese el legajo del alumno: "))

qAprobados = 0
qDesapro = 0
sumaNotas = 0
i = 0
while(i<len(notas)):
    if(notas[i]>=4):
        qAprobados = qAprobados + 1
    else:
        qDesapro = qDesapro + 1
    
    sumaNotas = sumaNotas + notas[i]
    
    i = i + 1

promNotas = sumaNotas/len(notas)

legajosMayores = []
j = 0
while(j<len(notas)):
    if(notas[j]>promNotas):
        legajosMayores.append(legajos[j])
    j = j + 1

print(qAprobados)
print(qDesapro)
print(promNotas)
print(legajosMayores)