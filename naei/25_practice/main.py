#لیست امتیازات دانش آموزان

names = ["amir", "hooshang", "reza", "mohsen", "mohammad"]
scores = [5, 7, 12, 8, 10]

for j in range(len(names)):

   print(names[j], int(scores[j]) *"*")

while  True:
    a = input("enter your name : ")
    if a == "0":
        break
    i = a in names
    if i:
        x = names.index(a)
        b = scores[x] * "*"
        print(a, b)
    else:
        print("no")


