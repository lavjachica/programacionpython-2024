factorial = int(input("Ingrese el número del cual desee obtener su factorial (x!) "))

numeros = []

total_factorial = 1

if factorial == 0:
    print(f"el resultado de {factorial}! es de 1. ")
else: 
    print(f"{factorial}! :")
    while factorial != 0 : 
        numeros.append(factorial)
        factorial -= 1
    for i in (numeros):
        total_factorial *= i
    print(f"{total_factorial}")
