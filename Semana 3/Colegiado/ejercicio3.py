producto=input("Ingrese el nombre del producto: ")
cantidad=int(input("Ingrese la cantidad: "))
precio=int(input("Ingrese el precio: "))

calculo=(cantidad*precio)*1.13

print("La cantidad de ",producto," que quieres comprar te costaria en total ya con el iva: ",calculo)
