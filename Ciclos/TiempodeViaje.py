viaje=1
suma=0
while viaje !=0:
    viaje=int(input("El/Los tiempos de viaje: cuando desees terminar ingresa (0) "))
    suma=suma+viaje
min=int(suma%60)
hrs=int(suma/60)

print("El tiempo total de viaje es: ", hrs,":",min,"horas")



   
