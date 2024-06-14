ciudad1= "Castro"
latitud1= -42.4721
longitud1= -73.77319
coordenadas1 = (latitud1, longitud1)

print(f"\n la ciudad de {ciudad1} su latitud es de {latitud1} y su longitud es de {longitud1}")
latitud1_ent = int(latitud1)
longitud1_ent = int(longitud1)
print(f"la latitud en entero es de : {latitud1_ent} y de longitud es : {longitud1_ent}")

ciudad2= "puerto montt"
latitud2= -41.4693
longitud2= -72.9423
coordenadas2 = (latitud2, longitud2)

print(f"\n la ciudad de {ciudad2} su latitud es de {latitud2} y su longitud es de {longitud2}")
latitud2_ent =int(latitud2)
longitud2_ent = int(longitud2)
print(f"la latitud en entero es de : {latitud2_ent} y de longitud es : {longitud2_ent}")

ciudad3= "concepcion"
latitud3= -36.82699
longitud3= -73.04977
coordenadas3= (latitud3, longitud3)

print(f"\n la ciudad de {ciudad3} su latitud es de {latitud3} y su longitud es de {longitud3}")
latitud3_ent= int(latitud3)
longitud3_ent= int(longitud3)
print(f"la latitud en entero es de : {latitud3_ent} y de longitud es : {longitud3_ent}")

coordenadas = (coordenadas1, coordenadas2, coordenadas3)
ciudades = [ciudad1, ciudad2, ciudad3]

print(type(coordenadas))
print(type(ciudades))

print(f"coordenadas almacenadas en tuplas: {coordenadas}")
print(f"ciudades almacenadas en listas: {ciudades}")