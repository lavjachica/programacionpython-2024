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
"""while True: 
    parametro = input(">")
    if parametro == "exit":
        break
    else: 
        print(parametro)"""
####Bucles
from colorama import init, Fore
print(Fore.GREEN + "Inicio de ciclo N1")
while num<= 200: 
    print(num)
    num = num + 2
    #num+=
print(Fore.YELLOW + "Inicio de Ciclo N2")
while num <= 200: 
    print(num)
    num = num + 2
else: 
    print(Fore.RED + "mi condicion es igual o mayor a 200")
print(Fore.YELLOW + "Cierre de ciclo N2")

print(Fore.CYAN + "Inicio de Ciclo N3")
while num <= 300:
    print(num)
    num = num + 2
    if num ==250: 
        print(Fore.YELLOW + "se detiene la ejecucion")
        break

print(Fore.CYAN + "Cierre de Ciclo N3")


print(Fore.LIGHTMAGENTA_EX + "Inicio de Ciclo N4")
newlista= [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)
print(Fore.LIGHTRED_EX + "")
for i in range(1,11): 
    print(i)
            