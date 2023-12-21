palabra = str(input("Ingresa la palabra: "))
pal_ = ""
for caracter in palabra:
    pal_ += "_"
print(pal_)

intentos = len(palabra)
palabra_lista = list(palabra)
palabra_oculta = list(pal_)
letras = []

while intentos > 0 and '_' in palabra_oculta:
    letra = input("Ingresa una letra: ").lower()
    
    if letra in letras:
        print("Ya has intentado esa letra. Intenta otra.")
        continue
    
    letras.append(letra)
    
    if letra in palabra_lista:
        for i, char in enumerate(palabra_lista):
            if char == letra:
                palabra_oculta[i] = letra
        print("¡Correcto!")
    else:
        partes_cuerpo = [
            "Cabeza",
            "Brazos",
            "Torso",
            "Pierna"]
    for i in range(intentos):
        print(partes_cuerpo[i])
    intentos -= 1
    print("Incorrecto. Intentos restantes:", intentos)
    
    print("Palabra:", ''.join(palabra_oculta))

if '_' not in palabra_oculta:
    print("Felicitaciones")
else:
    print("¡AHORCADO! La palabra era:", palabra)
