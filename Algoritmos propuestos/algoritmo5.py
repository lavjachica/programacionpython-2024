print("ingrese fecha de vencimiento de primer producto: ")
fecha1 = int(input("ingrese el dia: ")), int(input("ingrese el mes: ")), int(input("ingrese el año: "))

print("ingrese fecha de vencimiento de segundo producto: ")
fecha2 = int(input("ingrese el dia: ")), int(input("ingrese el mes: ")), int(input("ingrese el año: "))

print("ingrese fecha de vencimiento de tercer producto: ")
fecha3 = int(input("ingrese el dia: ")), int(input("ingrese el mes: ")), int(input("ingrese el año: "))

newtupla = tuple(fecha1)
newtupla2= tuple(fecha2)
newtupla3 = tuple(fecha3)
print(sorted(newtupla))
print(sorted(newtupla2))
print(sorted(newtupla3))

fechaorden = (sorted([fecha1,fecha2,fecha3]))
print(fechaorden)

fechaorden2 = (sorted([newtupla,newtupla2,newtupla3]))
print(fechaorden2)