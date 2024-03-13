st = int(input("Quieres tirar unos dados? (s/n)"))
import random
ran1 = random.randint(1, 6)
ran2 = random.randint(1, 6)
res = ran1 + ran2
rnd = 0
point = 0
while st == "s":
    while point < 7:
        while rnd == 0:
            if res == 7 or res == 11:
                print("Ganaste! ")
                break
            elif res == 2 or res == 3 or res == 12:
                print("Craps! You loose! ")
                break
            else:
                point = point + 1
                st = int(input("Tira de nuevo"))
      
        while rnd > 0:
            if ran1 == 7 or ran2 == 7




















