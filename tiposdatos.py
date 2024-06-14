import math

print("########STRINGS########\n")
institucion = "Universidad de los Lagos\n"
asignatura = 'programacion'
descripcion = """Asignatura de primer semestre de la carrera de Ing. Civil en Informatica\n"""

print(institucion[0]) #imprimir la posicion de un caracter, si colocamos un numero en negativo imprime de derecha a izquierda
 
#concatenacion 
resultado = print(institucion + " " + asignatura )
salida = print( institucion  * 4 ) #puede multiplicar la variable 
print(institucion.split()) #funcion split en strings 
print(len(institucion)) #funcion que cuenta la cantidad de carcateres en la variable  
#potencia 
estatura = 1.53
peso= 54 
imc= peso / (estatura ** 2) 
print(math.trunc(imc)) #deja la parte entera 
print(imc) #muestra la parte decimal 
#booleanos
print("##########BOOLEANOS############\n")
ampolleta = False
interruptor = True 

print(type(ampolleta),type(interruptor)) #muestra el tipo de dato 
print(type(imc))
print(type(peso))
#Salidas de booleanos 

print(1 <= 0 )
print(100 >= 10) 
print(19 == 19)
print("####OPERADOR_BOLEANOS###\n")
#operador booleano 
print(bool(0))
print(bool(1))
print(bool("false"))
print(bool(""))
print(bool([]))
print("######CREANDO_UNA_LISTA########\n")
ciudades = ["Catro", "Dalcahue", "Ancud", "Quellon", "Chonchi"]
varios = ["Nicolas", 20, True]
list = ("python", "Ruby") #otro tipo de lista 

print(type(ciudades))
print(ciudades)
print(varios)
print(list) 

#cantidad de elementos de una lista 
print(len(ciudades))
print(ciudades.count("Dalcahue")) #cuenta la cantidad de ocurrencias de un elemento 

#tuplas 
musica = tuple()
generos = ("rock", "Blues", "Pop")
print(generos)
print(type(generos))

print(generos[2])
print(tuple.index("pop"))
print(len(ciudades))

#generos[0] = "cumbia" (propiedad de inmiutabilidad)
#cambio de estructura (tupla a lista)
tuplita = ("victor", 200, "univerisdad", True)
print(tuplita)
tuplita = list(tuplita)
print("la tupla ahor es de tipo", type(tuplita))
#tomando un trozo de la tupla 
print(tuplita[0:3])
# sets (conjuntos)
conjunto_vacio = set() #inicializando un set 
conjunto_x = {"javascript"}
print(type(conjunto_vacio))
print(type(conjunto_x))
#inicializando sets 
colores = {"azul","rojo","amarillo", "verde", "violeta"}
animales = set({"gato", "perro", "caballo", "hamster"})

print(colores)
print(animales)

#agregando un nuevo elemento al set
colores.add("celeste")
print(colores)
#reasignando valores de listas
listrum= (1,2,3,4,5,6,7,8,9,10)
listrum2= list(range(1,1001,10)) #rango
#elemento especifico 
print(ciudades[3])
print(ciudades.count("castro")) #cantidad de ocurrencias de un elemento 
ciudades[0] = "quemchi" #reasignando variable 
print(ciudades)
#tuplas son inmutables
newtupla = ("daniel","pedro", 300)

#diccionarios (conjuntos)
paciente = dict(
    nombre= "Francisco",
    edad= 30,
    ciudad= "castro")
hospital = { "nombre" : "Augusto Riffart" , "ciudad" : "Catro" } 

doctor = {
    "nombre" : "Elson",
    "edad" : 40,
    "especialidad" : "cirujano"}
#eliminando la clave "nombre" del diccionario doctor 
doctor.pop("nombre")
print("diccionario actualizado:", doctor)
#consultar valores y claves
print(paciente.keys())
print(paciente.values())

#consultar valores especificos 
print(paciente["nombre"]) #imprime el nombre de diccionario paciente 

#actualizar diccionarios 
paciente.update({
    "ciudad" : "queilen",
    "Edad" : 40})
print(paciente)

paciente.clear() #para eliminar diccionario
print(paciente)

