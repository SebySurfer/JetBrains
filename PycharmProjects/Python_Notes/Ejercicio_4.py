n1 = int(input("Dame lado 1 del triangulo: "))
n2 = int(input("Dame lado 2 del triangulo: "))
n3 = int(input("Dame lado 3 del triangulo: "))


if (n1 > n2) and (n1 > n3):
    if ((n2**2 + n3**2) == n1**2):
        print("Si es un triangulo rectangulo")
    else:
        print("No es un triangulo rectangulo")
elif (n2 > n1) and (n2 > n3):
    if ((n3**2 + n1**2) == n2**2):
        print("Si es un triangulo rectangulo")
    else:
        print("No es un triangulo rectangulo")
elif (n3 > n1) and (n3 > n2):
    if ((n1**2 + n2**2) == n3**2):
        print("Si es un triangulo rectangulo")
    else:
        print("No es un triangulo rectangulo")
