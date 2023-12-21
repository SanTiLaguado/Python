palabra=str(input("ingrese la palabra: "))
pal_ = ""
for caracter in palabra:
    pal_ += "_"
print(pal_)
int=len(palabra)
listpal = list(palabra)
letras=[]
while int > 0 and '_' in pal_:
    letra = input("Ingresa una letra: ").lower()
    if letra in letras:
        print("Ya has intentado esa letra. Intenta otra.")
        continue
    letras.append(letra)
    
    if letra in listpal:
        for i, char in enumerate(listpal):
            if char == letra:
                pal_[i] = letra
        print("Correcto")
    else:
        int -= 1
        print("Incorrecto. Intentos restantes:", int)
    
    print("Palabra:", ''.join(pal_))

if '_' not in pal_:
    print("Ganaste!")
else:
    print("Ahorcado:", palabra)
    