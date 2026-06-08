#identificadores y variables
#variable con sake_case

nombre_alumno = "angel joaquin"
edad_alumno = 19
promedio_final = 9.8

#constantes con SCREAMING SNAKE CASE
TASA_IVA = 0
CALIFICACION_MINIMA = 7.0
PESO_PARCIAL = 0.20
PI = 3.1416
GRAVEDAD_PLANETA = 9.84
CAPACIDAD_MAXIMA_SALON = 25


#Tipado dinamico - la variable cambia de tipo
dato = 100
print(type(dato))
dato = 'cien'
print(type(dato))

#uso de constantes en un calculo
precio_base = 500.0
precio_final = precio_base * (1 + TASA_IVA)
print(f'Precio con IVA: ${precio_final:.3f}')

#Define 3 constantes: PESO_PARCIAL=0.20,PESO_PROYECTO=0.40 y CALIFICACION_MINIMA=6.0. Luego crea 4 variables con calificaciones y calcula el promedio ponderado usando las constantes. Imprime si el alumno aprobó o reprobó

PESO_PARCIAL = 0.20
PESO_PROYECTO = 0.40
CALIFICACION_MINIMA = 6.0
parcial_1 = 5.5
parcial_2 = 5.0
proyecto_1 = 5.0
proyecto_2 = 6.5
suma_pesos = PESO_PARCIAL + PESO_PARCIAL + PESO_PROYECTO + PESO_PROYECTO
nota_ponderada = (parcial_1 * PESO_PARCIAL) + (parcial_2 * PESO_PARCIAL) + (proyecto_1 * PESO_PROYECTO) + (proyecto_2 * PESO_PROYECTO)
promedio_final = nota_ponderada / suma_pesos
print(f"El promedio final ponderado es: {promedio_final:.3f}")

if promedio_final >= CALIFICACION_MINIMA:
    print("Estado: APROBADO")
else:
    print("Estado: REPROBADO")