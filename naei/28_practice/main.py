list =[]
d = {}

while True:
    name=input("name : ")
    if name == "0":
        break
    else:
        d["name"] = name
    age=input("age : ")
    d["age"] = age

    city=input("city : ")
    d["city"] = city

    list.append(d)

print(list)
