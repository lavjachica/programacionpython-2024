####Crea un algoritmo que permita adivinar un número. En primer lugar el algoritmo debe  solicitar un número entero por consola. A continuación va pidiendo números y varespondiendo si el número a adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número.

num_adivinar = int(input("ingrese un numero, que despues el programa intentara adivinar: "))
num = int(input("Adivina el numero: "))
while num_adivinar != num: ### mientras el numero a adivinar sea distinto de el numero ingresado entonces:
    if num_adivinar > num: ### si el numero a adivinar es mayor que el numero ingresado entonces:
        print(f"El numero que haz ingresado es menor al numero a adivinar:") ###se muestra en pantalla
        num = int(input("Ingrese otro numero: "))
    elif num_adivinar < num: ##### sino, si el numero a adivinar es menor que el numero ingresado entonces:
        print("El numero que haz ingresado es mayor al numero a adivinar: ")
        num = int(input("ingrese otro numero: "))
  ####### el numero no es mayor ni menor entonces: 
print("Adivinaste el numero")