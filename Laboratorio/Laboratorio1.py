#inicializando variables 
manzana = int(100)
pera = int(250)
durazno = int(300)
cant_man = int(150)
cant_Pera = int(80)
cant_duraz = int(120)
#obtener el total de precio por cada fruta
totalM= (manzana * cant_man)
totalP= (pera * cant_Pera)
totalD= (durazno * cant_duraz)
totalMYP= (totalM + totalP)
preciototal= (totalM, totalD, totalP)
#imprimiendo el valor de total a pagar por cada tipo de fruta
print(f"El valor total a pagar por las manzanas es de: {totalM}")
print(f"El valor total a pagar por las peras es de: {totalP}")
print(f"El valor total a pagar por los duraznos es de: {totalD}")
#imprimiendo el valor a pagar solo por MANZANAS Y PERAS
print(f"El valor a pagar por manzanas y peras es de: {totalMYP}")
#el valor maximo entre los tres totales
valormax = max(preciototal)
print(f"el valor maximo a pagar de entre los precios de las tres frutas es de: {valormax}")
#el valor minimo entre los tres totales
valormin = min(preciototal)
print(f"el valor minimo a pagar de entre los precios de las tres frutas es de: {valormin}")
#calcular el promedio 
sumapromedio = (manzana + pera + durazno)
promediofinal = ((sumapromedio)/3)
print(f"el promedio entre el precio de las tres frutas es de: {promediofinal}")
print('el promedio final redondeado es de', (round(promediofinal,2)))
