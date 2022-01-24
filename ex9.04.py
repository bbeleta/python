"""
Crea un programa que imprima al azar 0 o 1.
En lugar de 0 o 1, que imprima cara o cruz.
Añádele un bucle para que lo haga 50 veces.
Crea una suma acumulada para el total de veces que salió cara y las que salió cruz.
"""
#Ejercicio 9 del capítulo 04
#Bel Santandreu Nadal

cara = 0
creu = 0

import random
for i in range(50):
    moneda = ["cara", "creu"]
    random_index = random.randrange(2)
    print(moneda[random_index])
    if moneda[random_index] == "creu":
        creu += 1
    elif moneda[random_index] == "cara":
        cara +=  1

print("cara: ",cara)
print("creu: ",creu)