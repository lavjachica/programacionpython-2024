### determinar si una palabra ingresada por teclado es un palindromo. eliminar espacios 
### y convertir el texto ingresado a minusculas, Ademas imprimir la palabra invertida
cadena = input("ingrese un texto porfavor: ")
cadena_invertida = "" ### guarda valores
for i in range (len(cadena)):
    cadena_invertida += cadena[-(i+1)]  ### el i toma el valor del recorrido
print(f"Texto invertido: {cadena_invertida}")               ## entonces ej : [-(0+1)] = [-1] asi consecutivamente
print(f"el texto en minusculas: {cadena_invertida.lower()}")

if cadena == cadena_invertida:                          #####funciona con una palabra con texto no
    print("la palabra o el texto es un palindromo")
else:
    print("la palabra o el texto no es un palindromo")