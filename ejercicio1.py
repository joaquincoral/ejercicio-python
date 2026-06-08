#REALIZADO POR: Angel Joaquin Coral LLaguno
#Este es un comentario de una linea

#Este es un comentario
#Que ocupa varias lineas

"""Este es otro ejemplo
de comentario multilinea"""

"""Este es otro ejemplo
de comentario multilinea"""

entero = 50 #Numeros enteros
decimal = 3.1416 #Numero decimales (float)
logico = True #Boolean
nombre = "Juan" #String

print(type(entero))
print(type(decimal))
print(type(logico))
print(type(nombre))

#Declara variables que almacene su nombre,apellido paterno,apellido materno, edad, estatura

nombre = "ANGEL JOAQUIN"
apellido_paterno = "CORAL"
apellido_materno = "LLAGUNO"
edad = 19
estatura = 1.68

print(nombre)
print(apellido_paterno)
print(apellido_materno)
print(edad)
print(estatura)

#list, tuple, set, dict, arrays, range, frozenset

#str
nombreMateria = "programacion"
print(nombreMateria[0])
print(nombreMateria[-1])
print(nombreMateria[0:6])

#list - mutable
calificaciones = [8.5,9.0,7.5,10.0]
calificaciones.append(9.5)
calificaciones[0] = 8.0
print(calificaciones)

#tuple - inmutable
coordenadas = (19.4326, -99.1332)
print(coordenadas[0])

# dict - clave:valor
alumno = {'nombre': 'Angel joaquin', 'edad': 19, 'promedio': 8.9}
print(alumno['nombre'])
alumno['promedio'] = 9.0
print(alumno)

#crea un diccionario con TUS datos: nombre, edad y materia favorita. imprime solo tu nombre accediendo a la clave correta

Diccionario = {
    "nombre": "Angel Joaquin",
    "edad": "19", 
    "materia_favorita": "matematicas"}
print(Diccionario["nombre"])
