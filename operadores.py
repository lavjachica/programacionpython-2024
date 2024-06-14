
print("\n################## OPERADORES LOGICOS #####################")
encendido= True 
edad= 19
bencina = True

print("\n #### VALOR AND ####")
if encendido and bencina: 
    print("el vehiculo puede avanzar. ")
else: 
    print("el vehiculo no puede arrancar")

####OPERADOR OR
print("\n #### VALOR OR ####")
if bencina or encendido:
    print("el vehiculo puede avanzar .")
else:
    print("el vehiculo no puede arrancar")

##DECLARANDO VARIABLES
a=20
b=3
c= 15
d= 6
print("\n################## OPERADORES ARITMETICOS ##################")

print("hola" * (int((10*2) / 5)), "\n")
print("\n### OPERADORES DE COMPARACION EN STRINGS #########")
animal_domestico = "gato"
animal_salvaje = "pato"
print(animal_domestico == animal_salvaje)
print(animal_domestico != animal_salvaje)
print(animal_domestico > animal_salvaje)
print(animal_domestico < animal_salvaje) 
print(animal_domestico >= animal_salvaje)
print(animal_domestico <= animal_salvaje)

("\n ############## BUCLE, CICLOS, LOOPS #######")
##### WHILE ITERACIONES NO DEFINIDAS (MIENTRAS EN PSEINT)
#while true: 
    #print(num)
    #num+=2            ###while infinito control C PARA INTERRUMPIR UN BUCLE INFINITO 
num= 0 
while num <= 100: 
    print(num)
    num += 2

while num <= 100: 
    print(num)
    num+= 2
else: 
    print("mi condicional es mayor o igual a 100")

####### uso del break 
while True: 
    parametro = input(">")
    if parametro == "exit":
        break
    else: 
        print(parametro)
            



