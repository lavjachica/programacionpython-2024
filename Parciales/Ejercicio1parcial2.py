
##### temperaturas en set
Temperaturas_Mínimas = {9, 5, 2, 7, 6, 1}
Temperaturas_Máximas = {12, 14, 11, 10, 15, 9}
##### A) verificar si la temperatura 9° se encuentra en ambos sets utilizando condicionales 
datos =  9 in Temperaturas_Mínimas and 9 in Temperaturas_Máximas ### verificando que el dato se encuentre en cada set
print(f"¿El dato '9°'aparece en ambos sets? {datos}") 
##### B) unir ambos sets en uno solo y eliminar duplicados, imprimir set generado
##### C) transformar el set en una lista y encontrar la temperatura minima y maxima
lista1= list(Temperaturas_Mínimas)
lista2= list(Temperaturas_Máximas)  
lista_t = (lista1 + lista2)  ###### set transformado en lista
suma_set = set(lista_t) ##### devolviendo a set
print(type(suma_set)) #### confirmando que sea un set
print(f"La union de los sets sin los duplicados es de: {suma_set}")
##### c) encontrado la temperatura minima y maxima UTILIZANDO BUCLES 
list_valores= []
for i in lista_t:
    if i == min(lista_t):     
        print(f"Temperatura minima: {i}") 
        list_valores.append(i)
        
for b in lista_t:
    if b == max(lista_t):
        print(f"temperatura maxima: {b}")
        list_valores.append(b)


##### D) crear una tupla con  los valores de temperatura minima y maxima, mas un string con las etiquetas de texto: Minima y maxima
print(tuple(f"Minima y Maxima: {list_valores}"))
##### E) Generar e imprimir un diccionario donde las claves sean las temperaturas 
# y los valores sean la frecuencia de aparicion
temperaturas_min = dict(
    temperatura_9= 1,     #### un diccionario simple c:
    temperatura_7= 1,
    temperatura_6= 1,
    temperatura_5= 1,
    temperatura_2= 1,
    temperatura_1= 1
)
temperaturas_max = dict(
    temperatura_15= 1,
    temperatura_14= 1,
    temperatura_12= 1,
    temperatura_11= 1,
    temperatura_10= 1,
    temperatura_9= 1
)
print("las temperaturas de cada set con su frecuencia de aparicion: ")
print(temperaturas_min)
print(temperaturas_max)
