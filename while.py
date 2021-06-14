totalVentas = 0
monto=int(input("Ingrese el monto de una venta"))
while monto!= -1:
    totalVentas=totalVentas+monto
    monto=int(input("Ingrese el monto de la venta"))
print("El total de ventas es:", totalVentas)