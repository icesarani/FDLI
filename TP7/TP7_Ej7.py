def sumaMeses(listaQ, mes):
    vMes = mes - 1
    listaQ[vMes] = listaQ[vMes]+1
    return listaQ
    
    

listaQ = [0,0,0,0,0,0,0,0,0,0,0,0]
legajo = int(input("Ingrese el numero de legajo del alumno, ingrese -1 para finalizar el programa: "))
while(legajo!=-1):
    dia = int(input("Ingrese el dìa en el que nacio el alumno: "))
    while(dia<1 or dia>31):
        dia = int(input("Ingrese un valor correcto para el dia: "))
    mes = int(input("Ingese el mes en el que nacio el alumno: "))
    while(mes<1 or mes>12):
        mes = int(input("Ingrese un valor correcto para el mes: "))
    anio = int(input("Ingrese el año en el que nacio el alumno: "))
    while(anio<1 or anio>2021):
        anio = int(input("Ingrese un valor correcto para el año: "))
    cumpXAl = sumaMeses(listaQ, mes)
    legajo = int(input("Ingrese el numero de legajo del alumno, ingrese -1 para finalizar el programa: "))
    
for i in range(0,len(cumpXAl),1):
    j = i + 1 #mes en el que nos encontramos parados
    print("En el mes",j,"cumplen años un total de",cumpXAl[i],"alumnos")
    
mayN = cumpXAl[0]
mayQ = 0
    
for i in range(0,len(cumpXAl),1):
    if(cumpXAl[i]>mayN):
        mayN = cumpXAl[i]
        mayQ = i+1
    
print("El mes con más cumpleaños es",mayQ)