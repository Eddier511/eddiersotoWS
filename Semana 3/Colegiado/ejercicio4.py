entraH=int(input("Hora de entrada: "))
entraM=int(input("Minutos: "))
entraS=int(input("Segundos: "))
salH=int(input("Hora de salida: "))
salM=int(input("Minutos: "))
salS=int(input("Segundos: "))

horas=(salH-entraH)*3600
minutos=(salM-entraM)*60
segundos=salS-entraS
totalS=horas+minutos+segundos

print("El tiempo labora en segundos fue de: ",totalS," segundos")