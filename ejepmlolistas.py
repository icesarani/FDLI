legajos = []
notas = []

for i in range(5):
    leg = int(input("Ingrese el legajo del alumno: "))
    legajos.append(leg)

    nota = int(input("Ingrese la nota del alumno: "))
    notas.append(nota)

print(notas)
print(legajos)
len(legajos) #te dice la cantidad de valores q almacena la lista
print(legajos[1]) #se muestra el elemento en la posicion 1

listNumeros = [1,2,3,4,5]
listNumeros.pop() #elimina el ultimo valor
print(listNumeros)
listNumeros.pop(2) #elimina el valor de la posicion n2
print(listNumeros)