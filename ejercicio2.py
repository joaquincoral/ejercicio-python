# - casting basico
# Implicita: int + float = float automaticamente
resultado = 5 + 2.0
print(resultado)
print(type(resultado))

#Emplicita: str a int
texto_numero = '42'
numero_real = int(texto_numero)
print(numero_real + 8)

#Explicita: int a str para concatenar
edad = 28
mensaje = 'Hola, soy joaquin y mi edad es ' + str(edad)
print(mensaje)

#float a int
precio = 9.99
print(int(precio))

numero = 7.35
redondeado = round(numero)
print(redondeado)

#simularemos input con variantes fijas
datos_usuario = '25'
print(type(datos_usuario))
#print(datos_usuario + 5)

edad_correcta = int(datos_usuario)
print(edad_correcta + 5)

#patron correcto para entrada de datos:
edad = int(input('ingresa tu edad'))

#Escribre un programa que pida al usuario su nombre (str) y su año de nacimiento (int). calcula e imprime su edad aproximada restando al año actual (2026).

nombre = input("Por favor, introduce tu nombre: ")
año_nacimiento = int(input("Por favor, introduce tu año de nacimiento: "))
edad = 2026 - año_nacimiento
print(f"Hola {nombre}, tu edad aproximada en 2026 es {edad} años.")

