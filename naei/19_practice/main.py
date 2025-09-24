#برسی بخش پذیری عدد ورودی بر 5

x = int(input("enter your number:"))

if x % 5:
    print("no")
else:
    print("yes")

#بزرگ ترین عدد دریافت شده

x = float(input("x:"))
y = float(input("y:"))
z = float(input("z:"))
max = 0
if x > max:
    max = x
if y > max:
    max = y
if z > max:
    max = z

print("max" + str(max))


#ورود با نام کاربری و رمز عبور

username = input("enter your username:")
password = input("enter your password:")


if (username == "amirhossein" and password == "12345" )\
    or ( username == "hoshang" and password == "009922")\
    or (username == "manizhe" and password == "00000")\
    or (username == "mahsa" and password == "m11m3"):
    print("ok")
else:print("error")




