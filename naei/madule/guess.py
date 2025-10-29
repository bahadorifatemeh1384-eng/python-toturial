import random

num = random.randint(1,100)

while 1 :
    a = int(input("enter a number: "))

    if a == num:
        print("you are the winner!")
        break
    if a > num:
        print("The number is smaller")
    if a < num:
        print("The number is biger")