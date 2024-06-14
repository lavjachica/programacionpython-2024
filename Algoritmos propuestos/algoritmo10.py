print("\n PRIMER ESTUDIANTE")
estudiante1 = input("¿cual es su nombre?")
carrera1 = input("¿cual es su carrera?")
lab11 = float(input("1° nota de laboratorio"))
lab12 = float(input("2° nota de laboratorio"))
notas1 = (lab11, lab12)

print("\n SEGUNDO ESTUDIANTE")
estudiante2 = input("¿cual es su nombre?")
carrera2 = input("¿cual es su carrera?")
lab21 = float(input("1° nota de laboratorio"))
lab22 = float(input("2° nota de laboratorio"))
notas2 = (lab21, lab22)

print("\n TERCER ESTUDIANTE")
estudiante3 = input("¿cual es su nombre?")
carrera3 = input("¿cual es su carrera?")
lab31 = float(input("1° nota de laboratorio"))
lab32 = float(input("2° nota de laboratorio"))
notas3 = (lab31, lab32)

estudiantes = {
    estudiante1 : carrera1,
    estudiante2 : carrera2,
    estudiante3 : carrera3
}

print(f"{estudiante1}: {estudiantes[estudiante1]} con notas {lab11, lab12}")
print(f"{estudiante2}: {estudiantes[estudiante2]} con notas {lab21, lab22}")
print(f"{estudiante3}: {estudiantes[estudiante3]} con notas {lab31, lab32}") 