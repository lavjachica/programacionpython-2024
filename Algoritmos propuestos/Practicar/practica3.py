turno_diurno = 12000
turno_nocturno = 16000
aumento = 12000 + 2000
nocturno = 16000 * 3000
primer_empleado = ((turno_nocturno * 3) + (turno_diurno * 2))
segundo_empleado = ((turno_nocturno * 3) + aumento)
tercer_empleado = ((turno_diurno * 3) + (turno_nocturno) + (nocturno))
empleado_1 = dict(
    Lunes= turno_nocturno,
    Martes= turno_nocturno,
    Miercoles= turno_nocturno,
    Jueves= turno_diurno,
    Viernes= turno_diurno,
    Sueldo_semanal= primer_empleado
)
empleado_2 = dict(
    Martes= turno_nocturno,
    Miercoles= turno_nocturno,
    jueves= turno_nocturno,
    Domingo= aumento,
    sueldo_semanal= segundo_empleado
)
empleado_3 = dict(
    Miercoles = turno_diurno,
    Jueves= turno_diurno,
    Viernes= turno_diurno,
    sabado= turno_nocturno,
    Domingo= nocturno,
    sueldo_semanal= tercer_empleado
)
empleados = dict(
    Empleado_N1 = empleado_1,
    Empleado_N2 = empleado_2,
    Empleado_N3 = empleado_3
)

print(f"los sueldos a ganar por dia y por semana de cada empleado son de: {empleados}")