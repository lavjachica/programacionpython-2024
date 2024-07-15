n = int(input("ingrese el N° de cubos a calcular: "))
impar = 1 

for i in range(1, n + 1):
    suma_impares = 0
    numeros_impares = []

    for a in range(i):
        numeros_impares.append(impar)
        suma_impares += impar
        impar += 2
    print(f"{i}^3 = {suma_impares}")