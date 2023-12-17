C1=float(input("Ingrese la nota del certamen 1"))
C2=float(input("Ingrese la nota del certamen 2"))
Lab=float(input("Ingrese la nota del Laboratorio"))

C3=(3*6.0)-C1-C2

NC=(C1+C2+C3)/3
NF=(NC*0.7)+(Lab*0.3)

print("La nota necesaria para pasar con 6.0 es " + str(NF))