exp = False
var = [1]

for n in range(2, 101):
    for g in range(0, len(var)):
        if n % var[g] == 0 and var[g] > 1:
            exp = True

    if exp is False:
        var.append(n)

    exp = False

print(var)
