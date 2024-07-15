import random

numeros = [random.randint(40,350) for i in range(20)]
print(f"los numeros esocgidos son: {numeros}")
numero_escogido = int(input("escoge un numero: "))
cantidad = numeros.count(numero_escogido)
print(f"tu numero se repite {cantidad} vez/veces.")