Puntajes_Matemáticas = (55, 17, 93, 75, 88, 55, 55)
Puntajes_Química = (10, 85, 75, 88, 91, 75)
Puntajes_Programación = (68, 78, 85, 68, 82, 10)
contador = 0
duplicados = []
for i in Puntajes_Matemáticas:
    if Puntajes_Matemáticas.count(i) > 1:
        contador += 1
        if contador > 1:
            if i not in duplicados:
                duplicados.append(i)

for b in Puntajes_Química:
    if Puntajes_Química.count(b) > 1:
        contador += 1
        if contador > 1:
            if b not in duplicados:
                duplicados.append(b)

for c in Puntajes_Programación:
    if Puntajes_Programación.count(c) > 1:
        contador += 1
        if contador > 1:
            if c not in duplicados:
                duplicados.append(c)
######### Imprimir los valores duplicados de cada tupla
print(f"El/los puntajes duplicados de las materias de matematica, quimica y programacion: {duplicados}") 
######### Convertir cada tupla en una lista y ordenar las listas en orden descendente.
lista1 = sorted(list(Puntajes_Matemáticas), reverse= True)
lista2 = sorted(list(Puntajes_Programación), reverse= True)
lista3 = sorted(list(Puntajes_Química), reverse= True)
lista_delistas = sorted((lista1, lista2, lista3), reverse= True)
print(f"listas ordenadas son: {lista_delistas}")
######### Unir las listas anteriormente generadas en una sola y eliminar los duplicados.
lista_eliminar = list(set(lista1 + lista2 + lista3))
print(f"lista sin elementos repetidos: {lista_eliminar}")
print(type(lista_eliminar))
######### Encontrar el puntaje máximo y mínimo de la lista resultante.
print(max(lista_eliminar))
print(min(lista_eliminar))