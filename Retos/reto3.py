###listas
ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
ica = [134, 99, 245, 50]

###ciudadmasbajo
min_ica = min(ica)
indexMIN= ica.index(min_ica)
ciudad_minICA= ciudades[indexMIN]

##masalto
max_ica= max(ica)
indexMAX = ica.index(max_ica)
ciudad_maxICA = ciudades[indexMAX]
#clasificaciones
if 0 <= min_ica <= 50:
    clasificacionMIN= "buena"
elif 51 <=  min_ica <= 100:
    clasificacionMIN= "moderada"
elif 101 <= min_ica <= 150:
    clasificacionMIN= "Dañina para grupos sensibles"
elif 151 <= max_ica <= 200:
    clasificacionMAX= "Dañina para la salud"
elif 201 <= max_ica <= 300: 
    clasificacionMAX= "muy dañina para la salud"
else
    clasificacionMAX= "peligrosa"

print(f"la ciudad con el ICA mas bajo es {ciudad_minICA} con un ica ")