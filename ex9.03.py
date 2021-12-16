"""
Observa el siguiente código. Adivina lo que crees que producirá y escríbelo. Luego, ejecútalo y compara el resultado con tu suposición.
"""
#Ejercicio 8 del capítulo 03
#Bel Santandreu Nadal

"""
La solució "y" sortirà malament ja que diven que x és igual a 6 i això és fals perqué és igual a 5. És a dir, la solució sortirà "Buzz" perque la resposta de z, que és 5, és correcta. 
"""

x = 5
y = x == 6
z = x == 5
print("x=", x)
print("y=", y)
print("z=", z)
if y:
    print ("Fizz")
if z:
    print ("Buzz")