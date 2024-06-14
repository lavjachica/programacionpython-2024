print("al ingresar la descripcion, porfavor de mas de 40 caracteres. ")
descripcion1 = str(input("ingrese la descripcion del producto 1: "))
precio1 = int(input("¿Cual es su precio? "))
cantidad1 = int(input("¿Cuanta cantidad de producto hay?"))
#asegurar que tenga al menos 40 Caracteres
longitud1 = len(descripcion1) < 40 
descripcion2 = str(input("ingrese la descripcion del producto 2: "))
precio2 = int(input("¿Cual es su precio? "))
cantidad2 = int(input("¿Cuanta cantidad de producto hay? "))   
#asegurar que tenga al menos 40 caracteres
longitud2 = len(descripcion2) < 40 
#mostrando la longitud de cada descripcion 
print(f"¿la descripcion 1 alcanza 40 caracteres? {longitud1}")
print(f"¿la descripcion 2 alcanza 40 caracteres? {longitud2}")
#trasnsformar a mayusculas 
descrip_mayus = descripcion1.upper()
print(f"Descripcion del producto 1 en mayusculas: {descrip_mayus}")
descrip_mayus2 = descripcion2.upper()
print(f"Descripcion del producto 2 en mayusculas: {descrip_mayus2}")
#unir las palabras de cada descripcion con un espacio en blanco
unir1 = ' '.join(descrip_mayus.split())
unir2 = ' '.join(descrip_mayus2.split())
#mostrando en pantalla 
print(f"La descripcion unida 1 es: {unir1}")
print(f"La descripcion unida 2 es: {unir2}")
#valores de cada producto 
preciot1 = precio1 * cantidad1
preciot2 = precio2 * cantidad2
#mostrando el valor 
print(f"el valor total del primer producto en inventario es: {preciot1}")
print(f"el valor total del segundo producto en inventario es: {preciot2}")
total= preciot1 + preciot2
#mostrando en pantalla el total del producto 
print(f"el valor total de los productos 1 y 2 es de: {total}")
promedio = ((precio1 + precio2)/2)
#mostrando el promedio entre ambos precios
print(f"el promedio entre los precioes es de: {promedio}")
