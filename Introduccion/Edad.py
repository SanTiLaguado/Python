print("Ingrese sus datos de nacimiento")
dia=int(input("Dia:"))
mes=int(input("Mes:"))
año=int(input("Año:"))
from datetime import date
fecha_actual = date.today()

day = fecha_actual.day
month = fecha_actual.month
year = fecha_actual.year

print(day,month,year)

if (month, day) < (mes, dia):
    edad=(year-año)-1
    print("Usted tiene actualmente",edad,"años de edad")
else:
    edad=year-año
    print("Usted tiene actualmente",edad,"años de edad")