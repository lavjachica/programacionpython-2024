

# Secuencia inicial
secuencia = [500]

# Valores iniciales para las diferencias
diferencia = 44

# Variable para alternar la suma y resta
operacion_suma = False

# Generar números hasta alcanzar o superar 800
while secuencia[-1] < 800:
    if operacion_suma:
        siguiente_numero = secuencia[-1] + diferencia
    else:
        siguiente_numero = secuencia[-1] - diferencia

    secuencia.append(siguiente_numero)
    
    # Alternar la operación
    operacion_suma = not operacion_suma
    
    # Incrementar la diferencia para la siguiente operación
    if operacion_suma:
        diferencia += 10
    else:
        diferencia += 2

# Imprimir la secuencia generada
print(secuencia)



    
    