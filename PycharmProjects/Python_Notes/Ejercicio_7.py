n = int(input("Dame un numero para el factorial: "))

count = 1
c = 0
#Question = Why didn't it work when i had count <=n ?? When logically you want it to stop when its equal to number 4 ???
while count < n:
    res = count * n
    c = c + res
    print(c)
    count = count + 1

