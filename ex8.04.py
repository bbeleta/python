"""
Escribe un programa en Python que:
Le pida al usuario siete números
Imprima la suma total de esos números
Imprima la cuenta de las entradas positivas, las que sean iguales a cero, y las negativas. Emplea una cadena if, elif, else, en lugar de tres if consecutivos
"""
#Ejercicio 8 del capítulo 04
#Bel Santandreu Nadal

total = 0
positiu = 0
negatiu = 0 
zero = 0 
for i in range(7):
    x = int(input("Introdueix un número: "))
    if x > 0:
        positiu +=1 
    elif x < 0: 
        negatiu += 1
    else: 
        zero += 1
    total += x 
print("El total es:",total)
print("Positius: ",positiu)
print("Negatiu: ",negatiu)
print("Zeros: ",zero)
