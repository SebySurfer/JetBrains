x = int(input("CUanto quieres invertir?: "))
t = int(input("Por cuantos años?: "))
per = int(input("La tasa de interes: "))

count = 1
sal = 0
inter = 0

while t >= count:
    inter = round(x*(per/100))
    sal = round(inter + x)
    print("Periodo ", count, ": ", "Inicial: " , x ," ", "Interes: ", inter, "Final: ", sal)
    count = count + 1
    x = sal
