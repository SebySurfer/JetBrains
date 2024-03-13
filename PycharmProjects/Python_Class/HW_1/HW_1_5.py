import random

print("Cuanta gente quieres que entre para este obra de teatro? ")
peop = int(input())
print("Cuanto va a costar el ticket?")
cost = float(input())
print("**************************************************************************\n")

table = [["             ", "Edad       ", "Descuento    ", "Dinero descontado"],
         ["Categoria 1: ", "5-14       ", " 35%         $", ""],
         ["Categoria 2: ", "15-19      ", " 25%         $", ""],
         ["Categoria 3: ", "20-45      ", " 10%         $", ""],
         ["Categoria 4: ", "46-65      ", " 25%         $", ""],
         ["Categoria 5: ", "66 y mayor ", " 35%         $", ""]]

guest_list = [0, 0, 0, 0, 0]
disc = [0.35, 0.25, 0.10, 0.25, 0.35]

for _ in range(peop):
    age = random.randint(5, 100)

    if 5 <= age <= 14:
        guest_list[0] += 1
    elif 15 <= age <= 19:
        guest_list[1] += 1
    elif 20 <= age <= 45:
        guest_list[2] += 1
    elif 46 <= age <= 65:
        guest_list[3] += 1
    else:
        guest_list[4] += 1

    for x in range(1, 6):
        hold = guest_list[x-1] * cost * disc[x-1]
        table[x][3] = hold

for x in range(6):
    for y in range(4):
        print(table[x][y], end="")
    print(" ")

