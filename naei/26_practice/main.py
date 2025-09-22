print("1_add \n2_remove \n3_exit")
list = []

while True:
    choose = input("enter your choice : ")
    if choose == "1":
        name = input("name : ")
        list.append(name)
        print(list)
    elif choose == "2":
        name = input("name : ")
        list.remove(name)
        print(list)
    elif choose == "3":
        break