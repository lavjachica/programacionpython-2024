segundo = 0
minuto = 0
hora = 0

while hora != 24: 
    print(f"{hora:02}:{minuto:02}:{segundo:02}")

    segundo += 1
    if segundo ==60:
        segundo =0
        minuto += 1
        if minuto ==60:
            minuto = 0 
            hora += 1
