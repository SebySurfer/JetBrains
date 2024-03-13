import random
from decimal import Decimal

nin = [0] + [0.0] * 50
jov = [0] + [0.0] * 50
ad_j = [0] + [0.0] * 50
ad_m = [0] + [0.0] * 50

for i in range(50):
    age = random.randint(0, 99)

    if 0 <= age < 13:
        weight = random.uniform(1, 45)
        nin[0] += 1
        nin[i + 1] = weight
    elif 13 <= age < 30:
        weight = random.uniform(45, 100)
        jov[0] += 1
        jov[i + 1] = weight
    elif 30 <= age < 60:
        weight = random.uniform(45, 100)
        ad_j[0] += 1
        ad_j[i + 1] = weight
    else:
        weight = random.uniform(45, 80)
        ad_m[0] += 1
        ad_m[i + 1] = weight

lists = [nin, jov, ad_j, ad_m]

for i in range(4):
    total_weight = sum(lists[i][1:])
    lists[i].append(total_weight)

table = [
    ["Categoria      ", "Edad       ", "Cantidad", "Promedio"],
    ["Niños          ", "0 - 12     ", "", ""],
    ["Jovenes        ", "13-29      ", "", ""],
    ["Adultos        ", "30-59      ", "", ""],
    ["Adultos mayores", "60 y mas   ", "", ""]
]

for i in range(1, 5):
    table[i][2] = str(int(lists[i - 1][0]))
    table[i][3] = (lists[i - 1][-1] / lists[i - 1][0])

print("Resultados: ")

for x in range(5):
    for y in range(4):
        print(f"{table[x][y]:<18}", end="")

    print(" ")

print(" ")
print("Tabla de Frecuencias: ")

for i in range(4):
    print(f"{table[i + 1][0]}: ", end="")

    for x in range(100):
        if int(lists[i][0]) == x:
            break
        print("*", end="")

    percentage = round((lists[i][0] / 50.0) * 100)
    print(f" ({percentage}%)")
    print(" ")