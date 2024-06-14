#creando los sets con animales correspondientes 
aves= {"aguila", "pato", "canario"}
animales_terrestres= {"leon", "elefante", "nutria"}
animales_acuaticos= {"pato", "delfin", "nutria"}
#mostrando cada set
print("\n########## SETS ANIMALES INICIAL")
print(f"Aves: {aves}")
print(f"Animales terrestres: {animales_terrestres}")
print(f"Animales acuaticos: {animales_acuaticos}")
#agregando un animal nuevo a cada set
aves.add("loro")
animales_terrestres.add("tigre")
animales_acuaticos.add("foca")
#mostrando los sets actualizados 
print("\n############ SETS DE ANIMALES ACTUALIZADO")
print(f"Aves actualizado: {aves}")
print(f"Animales terrestres actualizados: {animales_terrestres}")
print(f"Animales acuaticos actualizado: {animales_acuaticos}")
#interseccion de los sets 
aves_interseccion = aves.intersection(animales_terrestres)
animalesT_interseccion = animales_terrestres.intersection(animales_acuaticos)
animalesM_interseccion = aves.intersection(animales_acuaticos)
#imprimiendo variable
print("\n################ SETS DE ANIMALES INTERSECCION #######")
print(f"Interseccion de aves con animales terrestres: {aves_interseccion}")
print(f"Interseccion de animales terrestres con animales acuaticos: {animalesT_interseccion}")
print(f"Interseccion de aves con animales acuaticos: {animalesM_interseccion}")