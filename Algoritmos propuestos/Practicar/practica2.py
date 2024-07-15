#### Construir un programa permita calcular e imprimir el resultado de la siguiente sumatoria:
#### S = 500 + 456 + 510 + 454 + 520 + 452 + ... + 800
secuencia = [500]
patron = 44
suma = False
while secuencia[-1] < 800:
    if suma:
        sgte_num = secuencia[-1] + patron
    else:
        sgte_num = secuencia[-1] - patron
        secuencia.append(sgte_num)
suma = not suma
if suma:
    suma += 10
else:
    suma += 2

print(sum(secuencia))
print(secuencia)
