nombre=input("Nombre: ")
unidades=int(input("Total de unidades vendidas: "))
precio=int(input("Precio del articulo vendido: "))

comision=(precio*unidades)*0.1

print("Nombre: ",nombre,"\nTotal de unidades vendidas: ",unidades,"\nPrecio del articulo: ",precio,"\nComision: ",comision)