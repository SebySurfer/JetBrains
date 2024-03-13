cont = input("Quieres calcular tu salario? (s/n) ")

while cont == 's':
    t = int(input("Horas trabajadas: "))
    res = 0
    if t <= 40:
        res = 100*t
        print("Pago: ", res)
        cont = input("Quieres calcular tu salario? (s/n) ")
    elif t > 40 and t <= 48:
        res = (100*t) + ((t-40)*200)
        print("Pago: ", res)
        cont = input("Quieres calcular tu salario? (s/n) ")
    elif t > 48:
        res = (100*t) + (8*200) + ((t-48)*300)
        print("Pago: ", res)
        cont = input("Quieres calcular tu salario? (s/n) ")







