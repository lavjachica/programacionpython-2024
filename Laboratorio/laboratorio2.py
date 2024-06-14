
########LETRA B
######nueva clave densidad para los rios
Densidad_losrios = (404432 / 18429)
redondeado1= float((round(Densidad_losrios, 1)))


#############lista de comunas
#########LETRA D
comunas_losrios= ["Rio bueno", "La union", "Paillaco"]

#######creando tuplas provincias, los rios
#####LETRA E
provincias_losrios = ("Ranco", "Valdivia")


############LETRA A
#######creando los subdiccionarios 
IDregion14 = dict(
    Nombre_Region= "Los Rios",
    Superficie= "18.429",
    habitantes= "404.432",
    densidad= redondeado1,
    capital= "Valdivia", ######LETRA C
    Comunas= comunas_losrios
)
IDregion14.update = dict(
    provincias=provincias_losrios
)
######nueva clave densidad para Magallanes
##########LETRA B
densidad_magallanes = (166533 / 1382291)
redondeado2 = float((round(densidad_magallanes, 1)))

#############creando lista comunas
#########LETRA D
comunas_magallanes= ["Cabo de Hornos", "Puerto Williams", "Porvenir"]

###########creando la tupla para provincias de magallanes
######LETRA E
provincias_magallanes= ("Antartida Chilena", "Magallanes", "Tierra del fuego", "Ultima Esperanza")

########LETRA A
####### subdiccionario
IDregion12 = dict(
    Nombre_Region= "magallanes",
    Superficie= "1.382.291",
    habitantes= "166.533",
    densidad= redondeado2,
    Capital= "Magallanes", #######LETRA C
    Comunas= comunas_magallanes,
    provincias= provincias_magallanes
)
######### LETRA A
censo_2017 = dict(  ##############diccionario principal
    region_1= IDregion14,
    region_2= IDregion12)
print("\n############## DICCIONARIO SIN MODIFICAR ###########")
print(censo_2017)
################ LETRA F
nombre_region = "Magallanes y Antartica chilena"
IDregion12["Nombre_Region"]=[nombre_region]
print("\n########### DICCIONARIO MODIFICADO ############")
print(censo_2017)

#############Letra H
lista1= IDregion12.keys()
lista2= IDregion12.values()
final= tuple(lista1)
final2 = tuple(lista2)
print(f"tupla de claves region Magallanes: {final}")
print(f"tupla de valores region Magallanes: {final2}")
Lista12= IDregion14.keys()
lista22= IDregion14.values()
final12= tuple(Lista12)
final22= tuple(lista22)
print(f"tupla de claves region de Los rios: {final12}")
print(f"tupla de valores region de Los Rios: {final22}")
