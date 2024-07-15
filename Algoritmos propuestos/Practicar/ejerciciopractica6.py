#### Desarrollar un algoritmo que solicite al usuario una cadena de texto y cuente cuántas veces
#### aparecen las vocales 'a', 'e', 'i', 'o' y 'u' en la cadena de texto. Utilizar ciclos para resolver el problema.
cadena = input("Ingrese porfavor un texto: ")
print("A continuacion aparecera la cantidad de veces que aparece a, e , i, o, u")
len(cadena)
contador_a= 0
contador_e= 0
contador_i= 0
contador_o= 0
contador_u= 0
for a in cadena:
    if a == "a":
        contador_a += 1
for b in cadena:
    if b == "e":
        contador_e += 1
for c in cadena:
    if c == "i":
        contador_i += 1
for d in cadena:
    if d == "o":
        contador_o += 1
for e in cadena:
    if e == "e":
        contador_u += 1

print(f"cantidad de ['a':{contador_a}]['e':{contador_e}]['i':{contador_i}] ['o':{contador_o}] ['u':{contador_u}] ")
