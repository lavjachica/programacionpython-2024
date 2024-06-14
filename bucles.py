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
            