# En un club se registra la hora y minuto de entrada y lahora y minuto de salida de los socios.
# El club necesita un sistema que le permita ingresar la hora y minuto de entrada y salida del socio y le calcule
# e informe cuantas horas y minutos permaneció en el club. (el club abre sus puertas a las 8hrs y cierra alas 22 hrs)
# Diseñar el programade forma quepermita ingresar varios sociosy calcule la permanencia en el club. Al finalizar informar:
#   Tiempo promedio de permanencia en el club
#   Cuál fue el mayor tiempo de permanencia

# Entradas: Hora de Entrada, Minuto de Entrada, Hora de Salida, Minuto de Salida, Numero del Socio
# Salida: Hora y Minutos de permanencia en el club, Tiempo Promedio de permanencia en el club, Mayor tiempo en el club

#Ingreso el Numero de Credencial del socio para tener un stop en el programa
#Mientras que el nro del socio sea != a -1 entonces:
# Ingreso las horas y minutos y valido su veracidad

#Inicializo contadores y variables que almacenan sumas
cont = 0
minutosTt = 0
tiempoMP = 0
nCredSoc = int(input("Ingrese el numero del socio: (Para terminar el programa ingrese -1)"))
while(nCredSoc != -1):
    horaE = int(input("Ingrese la hora de entrada al club: "))
    while(horaE<8 or horaE>22):
        horaE = int(input("La hora de entrada es incorrecta, ingrese una hora correcta"))
    mintE = int(input("Ingrese el minuto de ingtreso: "))
    while(mintE<0 or mintE>59):
        mintE = int(input("Esta ingresando un valor invalido para el minuto de entrada, elija un valor valido: "))
    horaS = int(input("Ingrese la hora en la que salio del club: "))
    while(horaS<horaE or horaS<8 or horaS>22):
        horaS = int(input("El valor ingresado es invalido, vuelva a ingresar la hora de salida: "))
    mintS = int(input("Ingrese el minuto en el que salio del club: "))
    while((horaS==horaE) and (mintS<=mintE))and(mintE<0 or mintE>59):
        mintS = int(input("El valor ingresado para el minuto de salida es invalido, ingrese uno nuevo: "))
        
    #pasaje a minutos
    minutosE = (horaE*60)+mintE
    minutosS = (horaS*60)+mintS
    #minutos transcurridos en el club
    minutosT = minutosS-minutosE
    
    #sumo minutos transcurridos para despues sacar el promedio
    minutosTt = minutosTt + minutosT
    
    #si el tiempo transcurrido es mayor al anterior se guarda
    if(tiempoMP<=minutosT):
        tiempoMP=minutosT
    
    #saco las horas de permanencia
    permanenciaHoras = minutosT//60
    #saco los minutos de permanencia dividiendo los minutos totales entre 60, restandole las horas y multiplicando
    #el resto por 60 que me daria los minutos
    permanenciaMinutos = ((minutosT/60)-(permanenciaHoras))*60
    
    print("El socio permanecio",permanenciaHoras,"hora/s y",permanenciaMinutos,"minuto/s")
    
    cont=cont+1
    nCredSoc = int(input("Ingrese el numero del socio: (Para terminar el programa ingrese -1)"))
    
#Saco el promedio de minutos entre todos los socios
promT = minutosTt/cont
#Saco el promedio de horas por socio
horasProm = promT//60
#Saco el promedio de minutos restante en las horas por socio
mintsProm = ((promT/60)-horasProm)*60
print("El tiempo promedio de permanencia es de",horasProm,"horas y",mintsProm,"minutos")

horasM = tiempoMP//60
mintsM = ((tiempoMP/60)-horasM)*60
print("El mayor tiempo de permanencia fue de",horasM,"horas y",mintsM,"minutos")