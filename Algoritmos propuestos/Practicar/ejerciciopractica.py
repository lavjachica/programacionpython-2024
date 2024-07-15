Altura_zona_central = (8848, 8611, 8586, 8200, 8460, 8200)
Altura_zona_sur = (8848, 5567, 8125, 4560, 8051, 4560)
Altura_zona_austral = (2200, 2500, 1000, 2200, 3623, 990)
contador_C = 0
contador_S = 0
contador_A = 0
duplicados = []
for i in Altura_zona_central:
    if Altura_zona_central.count(i) > 1:
        contador_C += 1
        if contador_C > 1:
            if i not in duplicados:
                duplicados.append(i)

for a in Altura_zona_sur:
    if Altura_zona_sur.count(a) > 1:
        contador_S += 1
        if contador_S > 1:
            if a not in duplicados:
                duplicados.append(a)

for b in Altura_zona_austral:
    if Altura_zona_austral.count(b) >1:
        contador_A += 1
        if contador_S >1:
            if b not in duplicados:
                duplicados.append(b)
print(f"las alturas duplicadas de Zona central, sur y austral son : {duplicados}")
#### Verificar si la altura 8848m se encuentra en las tres tuplas utilizando bucles y
#### condicionales.
dato = (8848 in Altura_zona_central and 8848 in Altura_zona_sur and 8848 in Altura_zona_austral)
print(f"¿se encuentra 8848 en las tres zonas? {dato}")
#### C) Unir las tuplas en una sola y eliminar los duplicados.

tupla = tuple(set(Altura_zona_central + Altura_zona_sur + Altura_zona_austral))
print(f"variables sin repeticion: {tupla}")
print(type(tupla))
#### D) Transformar la tupla obtenida en una lista. Imprimir la nueva lista obtenida.
lista = list(tupla)
print(f"la nueva lista {lista}")
print(type(lista))
