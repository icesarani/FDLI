def asteriscos(cant):
    for i in range(cant):
        print("*",end="") #end funciona para elegir con q termina el print, si no se dice termina con el "enter"
    print()

def titulo(texto, cant):
    '''meustra una cantidad de asteriscos'''

    asteriscos(cant)
    print(texto)
    asteriscos(cant)


titulo("hola",6)