txt = input("Dame una frase: ")
n = int(input("Cuantas veces lo quieres repetir? "))
count = 0
#NOTE: Every function for WHILE LOOP has an independent variable count.
# If you have two WHILE LOOPS, they will count on their own in independent terms
#The system has its own count system
# If you make it count a certain number, it will store that variable and wont loose its memory UNTIL the LOOP breaks
while count < n:
    print(txt)
    count = count+1
    