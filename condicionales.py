"""
edad no valida < 0
niño/a <= 12
adoslecentes <= 17
adulto <= 64
adulto mayor <= 120
edad no valida >= 120
"""
edad =int(input("ingrese la edad de la persona: "))
if edad < 0 or  edad >= 120:
    categoria = "edad no valida"
elif edad <= 12:
    categoria = "Niño/a"
elif edad <= 17: 
    categoria = "Adoslecentes"
elif edad <= 64:
    categoria = "adulto"
elif edad <= 120:
    categoria = "adulto mayor"

print(f"la persona es: {categoria}")