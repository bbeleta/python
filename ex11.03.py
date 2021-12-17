"""
Observa el siguiente código. Adivina lo que crees que producirá y escríbelo. Luego, ejecútalo y observa si estabas en lo cierto. 
"""
#Ejercicio 11 del capítulo 03
#Bel Santandreu Nadal
"""
Durant l'exercici es van imposant una serie de condicions que nosaltres hem de comprovar. 
La condició 1 és certa perque 3 és igual a 3. 
La condició 2 és falsa perqué hi ha un espai que sobra entre les comilles i el nombre.
La condició 3 és vertadera perque 3 és més petit que 4. 
La condició 4 és vertadera perque 3 és més petit que 10.
La condició 5 és vertadera perquè la cadena 3 és més petita que la 4. 
La condició 6 és falsa perquè la cadena 3 és més gran que la 10. 
La condició 7 és falsa perquè en el true no hi ha d'haver comilles. 
La condició 8 és vertadera perque 2 és igual a 2. 
La condició 9 és falsa perque el nombre 3 no és més petit que la cadena 3. 
"""
print("3" == "3")
print(" 3" == "3")
print(3 < 4)
print(3 < 10)
print("3" < "4")
print("3" < "10")
print( (2 == 2) == "True" )
print( (2 == 2) == True )
print(3 < int("3"))
