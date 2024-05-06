#variable de nombre 
nombre = 'Carla'
print('mi nombre es', nombre)
#variable 2
nombre = 'belen'
estatura = '1.53'
print(f'hola mi nombre es {nombre}')
print('mi estatura es', estatura)
#concatenacion 
nombre = 'Carla'
Apellido = 'Vargas'
edad= 20 #para poder utilizar en una string variable numerica se utiliza el termino str antes de la variable
print("hola mi nombre es " + nombre + " " + Apellido + " y tengo " + str(edad) + " años")
print(f"hola mi nombres es {nombre} y tengo {edad} años") #otra forma de plantear lo mismo 
#utilizar input 
year = input("¿en que año naciste?") #escribir
print(f"el año de naicmiento ingresado es {year}") 
#declaracion de variables en una linea 
pais, region, ciudad, codigopostal = " Chile ", "Los Lagos ", "Catro ", 5700000
print(pais + region + ciudad + str(codigopostal)) #No muy recomendado 