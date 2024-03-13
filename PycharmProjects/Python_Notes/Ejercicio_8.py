count1 = 's'
count = 0
import random
ran = random.randint(1, 10)


while (count1 == 's'):
    num = int(input("Elige un numero que se eligio al azar: "))

    while count < 2:
        if num == ran:
            print("Congratulations!")
            count1 = input(print("Quieres intentar de nuevo?: (s/n)"))

        else:
            print("Intenta de nuevo!")
            num = (input(print("Elige un numero que se eligio al azar: ")))
            count = count + 1

        if count == 2:
            print("Buena jugada!, el numero era ", ran)
            count1 = (input(print("Quieres intentar de nuevo?: (s/n)")))







