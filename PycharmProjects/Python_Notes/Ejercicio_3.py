

n1 = int(input("Dame lado 1 del triangulo: "))
n2 = int(input("Dame lado 2 del triangulo: "))
n3 = int(input("Dame lado 3 del triangulo: "))

if (n1 == n2) and (n2 == n3) and (n1 == n3):
    print("El triangulo es Equilatero")
elif (n1 != n2) and (n2 != n3) and (n1 == n3):
    print("El triangulo es Isosceles")
elif (n1 != n2) and (n2 == n3) and (n1 != n3):
    print("El triangulo es Isosceles")
elif (n1 == n2) and (n2 != n3) and (n1 != n3):
    print("El triangulo es Isosceles")
elif (n1 != n2) and (n2 != n3) and (n1 != n3):
    print("El triangulo es Escaleno")
