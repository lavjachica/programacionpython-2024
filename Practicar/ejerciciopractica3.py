
cadena = input("Ingrese un texto de 150 caracteres: ")
print(len(cadena))
while len(cadena) != 150: #### mientras la cantidad de caracteres sea distinta de 150 se imprime otra vez hasta que sea de 150
    cadena = input("ingresa un texto de 150 caracteres: ")
contador = 0
for caracter in cadena: 
    if caracter == 'a':
        contador += 1
print(f"El carácter 'a' se repite {contador} veces en la cadena.")
