N=int(input("ingrese el numero de datos: "))
datos=[]
suma=0
datosm=0
for dato in range(N):
    dato=float(input("ingrese el dato: "))
    datos.append(dato)
    suma=sum(datos)
    promedio=suma/N
datosm=sum(1 for dato in datos if dato > promedio)
print(datosm,"datos son mayores que el promedio:",promedio)
