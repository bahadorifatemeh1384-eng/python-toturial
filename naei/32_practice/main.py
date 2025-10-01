#برسی زوج بودن عدد
num = int(input("number : "))
def check(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(check(num))


#خلاصه کننده متن
def summarize(t):
    return t[:100] + "..." if len(t) > 100 else t

t = input("enter your text: ")
print(summarize(t))


#بررسی کد پستی
code = input("code posti : ")

def check2(code):
    i = len(code) == 15 and code.isdigit()
    return i

print(check2(code))


#رمزنگاری جایگزینی
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text1 = input("enter : ")


def ramznegari(text1):
    text2 = []
    for i in text1:
        if i == " ":
            text2.append(" ")
            continue
        x = letters.index(i.upper())
        print(x)
        text2.append(letters[-x-1].lower()) if i.isupper() else text2.append(letters[-x-1].upper())

    return text2

text2 = "".join(ramznegari(text1))
print(text2)

def ramzgoshaee(text2):
    text3 = []
    for i in text2:
        if i == " ":
            text3.append(" ")
            continue
        y = letters.find(i.upper())
        text3.append(letters[-y-1].lower()) if i.isupper() else text3.append(letters[-y-1].upper())
    return text3

text3 ="".join(ramzgoshaee(text2))
print(text3)
