P1=input("Ingrese la primera palabra")
P2=input("Ingrese la segunda palabra")
L1=len(P1)
L2=len(P2)
if L1 > L2:
    dif=L1-L2

    print("La palabra mas larga es",P1,"Con",dif,"Letras mas que",P2)
else:
    dif=L2-L1
    print("La palabra mas larga es",P2,"Con",dif,"Letras mas que",P1)

