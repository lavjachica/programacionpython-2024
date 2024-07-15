
n = int(input("Ingrese el número de cubos a calcular: "))
impar = 1

for i in range(1, n + 1): ###n + 1 porque rondea al anterior
    suma_impares = 0
    numeros_impares = [] ###guarda los numeros impares
    for a in range(i): #### a itera en i que es el anterior for 
        numeros_impares.append(impar) ###### añade los numeros impares a la lista
        suma_impares += impar ##### muestra el valor final de los numeros elevados al cubo
        impar += 2 ##salta al siguiente numero impar (1+2 = 3, 3+2= 5, 5+2= 7)
       
    

      

    print(f"{i}^3 = {suma_impares}")
