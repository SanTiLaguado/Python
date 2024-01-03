def dato_numerico(enunciado):
    while True:
        dato=input(enunciado)
        if dato.isdigit():
            return int(dato)
            break
        else:
            print("El dato no es numerico, Ingrese un dato valido")

def dato_positivo(enunciado):
    while True:
        dato = input(enunciado)
        if dato.isdigit() and int(dato) > 0:
            return int(dato)
        else:
            print("Ingrese un dato válido")

def dato_cadena(enunciado):
    while True:
        dato = input(enunciado)
        if dato.isalpha():
            return dato
        else:
            print("Ingrese un dato válido")
 
def dato_rango(enunciado,menor,mayor):
    while True:
        dato = input(enunciado)
        if dato.isdigit() and int(dato) > 0:
            return int(dato)
        else:
            print("Ingrese un dato válido")