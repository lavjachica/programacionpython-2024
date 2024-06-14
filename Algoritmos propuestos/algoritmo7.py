#ingresando el nombre y edad de tres personas
nombre1= input("ingrese nombre de la primera persona: ")
edad1 = int(input("ingrese edad: "))

nombre2= input("ingrese nombre de la segunda persona: ")
edad2= int(input("ingrese edad: "))

nombre3= input("ingrese nombre de la tercera persona: ")
edad3= int(input("ingrese edad: "))

personas = {
    nombre1 : edad1,
    nombre2 : edad2,
    nombre3 : edad3
}

print("\n DICCIONARIO DE PERSONAS: ")
print(f"{nombre1}: {personas[nombre1]} años")
print(f"{nombre2}: {personas[nombre2]} años")
print(f"{nombre3}: {personas[nombre3]} años")

####actualizar diccionario 
nombre_new = input("ingrese un nuevo nombre: ")
edad_new = int(input("ingrese respectiva edad: "))
personas[nombre_new]= [edad_new]
##eliminar nombre
persona_sacar = input("ingrese el nombre de la persona que desea sacar del diccionario: ")
del personas[persona_sacar]

print("\n Diccionario actualizado: ")
nombres = list(personas.keys())
edades = list(personas.values())

print(f"{nombres[0]}: {edades[0]} años")
print(f"{nombres[1]}: {edades[1]} años")
print(f"{nombres[2]}: {edades[2]} años")