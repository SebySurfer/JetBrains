import random
import math
#IMPORTANT NOTE: We are going to be adding all the data in the same list for each throne, that way we dont get lost in the storage of data.
Casa_Velaryon = ["Casa Velaryon "]
Casa_Stark = ["Casa Stark    "]
Casa_Hightower = ["Casa Hightower"]
Casa_Lannister = ["Casa Lannister"]
Casa_Martell = ["Casa Martell  "]
Casa_Tyrell = ["Casa Tyrell   "]
Casa_Baratheon = ["Casa Baratheon"]

#We create a list of lists, that way we dont have to individually have to make a ForLoop for every single list
Casas_List = Casa_Velaryon, Casa_Stark, Casa_Hightower, Casa_Lannister, Casa_Martell, Casa_Tyrell, Casa_Baratheon

#We create and add our random numbers
for casa in Casas_List:
    for month in range(12):
        casa.append(random.randint(50, 1001))

#Sum the amount that resulted in the end for every throne
for casa in Casas_List:
    sum = 0
    for x in range(12):
        sum += casa[x+1]
    casa.append(sum)

denom = 0
turn = 0
menorC = ""
menorN = 0
for casa in Casas_List:
    denom += casa[13]
    if turn == 0:
     menorN = casa[13]
     menorC = casa[0]
     turn += 1
    elif turn == 1:
        if casa[13] < menorN:
         menorN = casa[13]
         menorC = casa[0]


print()
print("                GAME OF THRONES")
print("----------------------------------------------")
print()
print("Lista de aportaciones totales por cada casa")
for casa in Casas_List:
    print(casa[0], ": ", "$", casa[13])
print()
print("La casa que aporto menos y quien se sentenciará a muerte es ", menorC, ", con solo $", menorN, " de ganancia.")
print("Primero, preguntamos al rey si se desea un Juicio de Combate")
print("...")

resp = random.randint(1, 101)

if resp >= 50:
    print("Tiene una oportunidad de vivir bebe", " -El Rey PachecoBebe")
else:
    print("El Lord de la moscas ... a perdon, de la CASA, ha muerto. xde    -El Rey PachecoBebe")

print()
print("Grafico de frecuencias: ")

#We'll add the number that represents the % of contribution a throne has made, and follow it up with a list of stars that it represents
for casa in Casas_List:
    casa.append(round((casa[13] / denom) * 100))
    for x in range(casa[14]):
        casa.append("*")

for casa in Casas_List:
    print(casa[0], ": ", end='')
    n = 15
    while n < len(casa):
        print(casa[n], end='')
        n += 1
    print(" ",casa[14], "%")

print("")
print("")
print("Example List= ", Casa_Hightower)
print()

#NOTE: I organized it in such a way that works like binary code. You have a string of values and you translate it to information.
#IMPORTANT NOTE: This is why OOP is better to handle all this information, because over time, it can be very easy to get lost




