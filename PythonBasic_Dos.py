#!/usr/bin/python3
"""Entrada de desde el teclado"""
#Primer caso
palabra = input("Introduce una palabra: ")
num_int = int(input("Introduce un numero: "))
num_float = float(input("Introduce un numero float: "))
num_complex = complex(input("Introduce un numero complejo: "))

print("String: ", palabra)
print("Entero: ", num_int)
print("Float: ", num_float)
print("Complejo: ", num_complex)

#segudno caso
nombre = input("¿Cual es tu nombre?: ")
print("Hola " + nombre + " vamos a hacer una suma")

num_uno = int(input("Por favor ingresa tu primer numero: "))
num_dos = int(input("Por favor ingresa tu segundo numero: "))

result = num_uno + num_dos

print(nombre + " tu resultado es ", result)

#Tercer caso
print("Sistema para calcular el promedio de un alumno")
nombre = input("Cual es tu nombre: ")

matematica = int(input(nombre + " ¿Cual es tu calificacion de matematicas?: "))
quimica = int(input(nombre + " ¿Cual es tu calificacion de quimica?: "))
biologia = int(input(nombre + " ¿Cual es tu calificacion de biologia?: "))

promedio = (matematica + quimica + biologia) / 3

if promedio >= 6:
    print("Felicidades " + nombre + ' "aprobastes :)" con un promedio de: ', round(promedio, 2))
else:
    print("Lo lamentamos " + nombre + ' "reprobastes:(" con un promedio de: ', round(promedio, 2))

print("Fin..")

