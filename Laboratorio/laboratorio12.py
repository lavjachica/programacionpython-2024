#ingresando la descripcion del articulo
print("INGRESE UN BREVE RESUMEN DEL ARTICULO IGUAL O MENOR A 60 CARACTERES")
Descripcion = input("ningrese el resumen del articulo: ")
#iniciando el contador de caracteres
contador = len(Descripcion)
ToF = (contador <= 60)
#imprimir la longitud 
print(f"la cantidad de caracteres es de: {contador}")

print(f"¿la descripcion cumple con igual o menor a 60 caracteres? {ToF}")
#convirtiendo el resumen a mayusculas 
mayus = Descripcion.upper()
print(f"la descripcion en mayusculas: {mayus}")
#mostrando los ultimos 10 caracteres del resumen
ult_caract = Descripcion[-10:]
print(f"los ultimos 10 caracteres del resumen son: {ult_caract}")
#uniendo las palabras con un guion
unir = '-'.join(Descripcion)
print(f"el texto con las palabras unidas usando guion como separador: {unir}")
