p1 = input("ingrese la 1° palabra clave: ")
p2 = input("ingrese la 2° palabra clave: ")
p3 = input("ingrese la 3° palabra clave: ")
p4 = input("ingrese la 4° palabra clave: ")
p5 = input("ingrese la 5° palabra clave: ")
palabras_clave = [p1,p2,p3,p4,p5]
 
lista_final = list(set(palabras_clave))
print(f"la lista original es de: {palabras_clave}")
print(f"la lista simple es de: {lista_final}")
