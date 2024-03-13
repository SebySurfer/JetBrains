
#Elabore un algoritmo que calcule la velocidad de impacto y el tiempo que
# tardará en caer un objeto en caída libre,
# conociendo la altura a la cual se deja caer.

h = int(input("Dame la altura: "))

import math

y = (2*h)/9.8
t = math.sqrt(y)
v = t*9.8

print("Time is: ", round(t, 2))
print("Velocidad es: ", round(v, 2))

