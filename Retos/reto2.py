#Crear un algoritmo que permita ingresar y gestionar las notas de un estudiante en tres asignaturas diferentes,
#utilizando diccionarios, tuplas, sets y listas. El algoritmo debe calcular el promedio final ponderado del estudiante
#por asignatura y mostrar toda la información ingresada.


######Profe hice mi mejor intento :) algo es
print("Bienvenido a la plataforma de notas Ulagos, ingrese los datos solicitados: ")
nombre_estudiante = input("ingrese su nombre: ")
nombre_asignatura = input("ingrese nombre de asignatura: ")
nota_lab1=float(input("ingrese la primera nota de laboratorio: "))
nota_lab2=float(input("ingrese la segunda nota de laboratorio: "))
nota_lab3=float(input("ingrese la tercera nota de laboratorio: "))
###########ngenerando los sets con las notas
notas_set1= {nota_lab1, nota_lab2, nota_lab3}
######promedio
promedio1= ((nota_lab1 * 0.30) + (nota_lab2 * 0.50) + (nota_lab3 * 0.20))
print(f"promedio {nombre_asignatura} es de {promedio1}")
nombre_asignatura2 = input("ingrese nombre de la segunda asignatura: ")
nota_lab12=float(input("ingrese la primera nota de laboratorio: "))
nota_lab22=float(input("ingrese la segunda nota de laboratorio: "))
nota_lab32=float(input("ingrese la tercera nota de laboratorio: "))
##########generando 2 set con  notas
notas_set2= {nota_lab12, nota_lab22, nota_lab32}
##########promedio
promedio2= ((nota_lab12 * 0.30) + (nota_lab22 * 0.50) + (nota_lab32 * 0.20))
print(f"promedio {nombre_asignatura2} es de {promedio2}")
nombre_asignatura3 = input("ingrese nombre de la tercera asignatura: ")
nota_lab13=float(input("ingrese la primera nota de laboratorio: "))
nota_lab23=float(input("ingrese la segunda nota de laboratorio: "))
nota_lab33=float(input("ingrese la tercera nota de laboratorio: "))
##########generando 3 set con notas
notas_set3= {nota_lab13, nota_lab23, nota_lab33}
#######promedio
promedio3= ((nota_lab13 * 0.30) + (nota_lab23 * 0.50) + (nota_lab33 * 0.20))
print(f"promedio {nombre_asignatura3} es de {promedio3}")
asignaturas = (nombre_asignatura, nombre_asignatura2, nombre_asignatura3)
notas = (notas_set1, notas_set2, notas_set3) 
promedio = ((promedio1 + promedio2 + promedio3)/3)
redondeado = (round(promedio, 1))

#########lista de tuplas
nombre_estudiante = (asignaturas, notas, redondeado)
########inicializando diccionario
nombre_estudiante = dict(
    nombre= nombre_estudiante,
    asignaturas= asignaturas,
    notas= notas,
    promedio= redondeado
)
print(nombre_estudiante)





