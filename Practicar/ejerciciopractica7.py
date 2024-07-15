###Escribir un programa que pida al usuario una cadena de texto y luego la invierta usando ciclos.
cadena = input("ingrese un texto porfavor: ")
print("A continuacion su texto se leera al reves.")
cadena_invertida = ""
for i in range (len(cadena)):
    cadena_invertida += cadena[-(i+1)]
print(cadena_invertida)
### Cuando i = 0, -(i + 1) es -1 (último carácter, 'a')
### Cuando i = 1, -(i + 1) es -2 (penúltimo carácter, 'l')
### Cuando i = 2, -(i + 1) es -3 (antepenúltimo carácter, 'o')
### Cuando i = 3, -(i + 1) es -4 (primer carácter, 'H')
### Por lo tanto, el bucle for iterará sobre los caracteres en el orden inverso.
