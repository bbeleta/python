"""
Escribe un programa que reciba un número del usuario e imprima si es positivo, negativo o cero.
"""
#Ejercicio 2 del capítulo 03
#Bel Santandreu Nadal

num = int(input("Digues un numero"))
if num > 0:
    print("Numero positiu")
elif num < 0:
    print("Numero negatiu")
else: 
    print ("Numero és igual a 0")

