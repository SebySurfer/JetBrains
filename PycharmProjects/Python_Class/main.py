

#Phrase
print("Hello world")
print("2+2= ", 4)

#Variables
a = 2
b = 3
c = a + b

#User Input
x = int(input("Give me a number: "))
print(x)

#Logical Commands

if x > 10:
    print("Bigger than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Less than 10")

#For Loop
for i in range(10):
    print(i)

#List or Array

ages = [18, 19, 17, 23, 32]

#tables

for i in ages:
    print(i)

while a < 10:
    print(a)
    a = int(input("Type a number for me "))

#Functions
def getting_ans(a,b):
    return a+b

print(getting_ans(4,5))

#True/False statements
t = True
f = False

#Lists

a = [0, 1, 2, 3, 4]
print(a)

a.append(3)


#Create number defined list

num_of_val = 5
alist = [0] * num_of_val



#Random numbers
import random
ran = random.randint(1, 3)

class Fruit:
    def __init__(self, name, color, num):
        self.name = name
        self.color = color
        self.num = num

apple = Fruit("apple", "red", 2)

print("This is a ", apple.name, ", and it is colored ", apple.color, " having ", apple.num*2)

