"""
¿Qué está mal en este código?
"""
#Ejercicio 12 del capítulo 03
#Bel Santandreu Nadal

print("Bienvenidos a la Ultra Trail!")
 
print("A. Banquero")
print("B. Carpintero")
print("C. Granjero")
 
entrada_usuario = input("¿Cuál es tu profesión?")
 
if entrada_usuario == "A":
    dinero = 100
elif entrada_usuario == "B":
    dinero = 70
else:
    dinero = 50
     
print("Genial! empezarás el juego con", dinero, "dólares.")
