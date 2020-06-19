#!/usr/bin/python3
"""Primera tarea realizando Gekkipedia de Ernesto"""
print('Esto es una suma')
numero_uno = 2
numero_dos = 4
result = numero_uno + numero_dos
print(result)

"""Manipulacion de cadena de Strings"""

"""Asignacion"""
mensaje = "Hola"
mensaje += " "
mensaje += "Deiwin"
print(mensaje)
print()
"""Concatenacion example"""
print("Concatenacion:")
mensaje = "Hola"
espacio = " "
nombre = "Deiwin"
print(mensaje + espacio + nombre)
numero_uno = 2
numero_dos = 4
result = numero_uno + numero_dos
result = str(result)
print("El resultado es: " + result)

"""Obtener sub cadenas de caracteres"""
print("Busqueda: ")
mensaje = "Hola Deiwin"
buscar_subcadena = mensaje.find("Deiwin")
print(buscar_subcadena)

"""Extraer sacar fuera de una cadena dependiendo de la posicion"""
print("Extraer: ")
mensaje = "Hola Deiwin"
extraer_subcadena = mensaje[1:6]
print(extraer_subcadena)

"""Comparacion de cadenas strings"""
print("Comparacion: ")
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)

"""Tipos de Datos"""
#Tipo de dato entero o largo
numero = 23
print(type(numero))
#imprimir numero
print(numero, type(numero))

#Tipo de dato flotante
numero_flotante = 23.3
print(numero_flotante, type(numero_flotante))

#Tipo de dato numero complejo
numero_complejo = 5 + 6j
print(numero_complejo, type(numero_complejo))

#Tipo de dato string
nombre = "Deiwin"
print(nombre, type(nombre))

#Tipo de dato boleano
verdadero_falso = 3 == 3
print(verdadero_falso, type(verdadero_falso))

