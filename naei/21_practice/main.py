# شمارش معکوس
from itertools import count

num= int(input("Enter a number: "))

for i in range(num+1):
    print(num-i)

#چاپ اعداد اول کوچک تر از a

a=int(input("Enter a number: "))

for i in range(1,a):
    for j in range(2,i):
        if i%j == 0:
           break
    else:
        print(i)


# اعداد صحیح بین دو عدد

a = int(input("a: "))
b = int(input("b: "))

for i in range(a+1, b):
    print(i)


#میانگین اعداد بی نهایت

c=0
sum=0

while i!=0 :

    i=float(input("Enter a number: "))
    if i==0:
        break
    c+=1
    sum=((sum*(c-1)) + i)/c
    print("current average" ,sum)

print("final average" ,sum)
