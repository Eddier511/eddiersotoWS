nombre=input("Nombre: ")
cedula=input("Cedula: ")
salario=int(input("Salario bruto: "))

calCCSS=salario*0.08
calBP=salario*0.01
totalded=calCCSS+calBP
salarioN=salario-totalded

print("Empleado: ",nombre,"\nIdentificacion: ",cedula,"\nSalario bruto: ",salario,"\nCCSS (8%): ",calCCSS,"\nBanco Popular (1%): ",calBP,"\nTotal deducciones: ",totalded,"\nSalario neto: ",salarioN)