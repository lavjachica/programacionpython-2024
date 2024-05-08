#1. Strings
institucion = "Universidad de los Lagos"
asignatura = 'programacion'
descripcion = """Asignatura de primer semestre de la carrera de Ing. Civil en Informatica"""

print(institucion[0]) #imprimir la posicion de un caracter, si colocamos un numero en negativo imprime de derecha a izquierda
 
#concatenacion 
resultado = print(institucion + " " + asignatura )
salida = print( institucion  * 4 ) #puede multiplicar la variable 
print(institucion.split()) #funcion split en strings 
print(len(institucion)) #funcion que cuenta la cantidad de carcateres en la variable   