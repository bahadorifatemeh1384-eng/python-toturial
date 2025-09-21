text= input("enter your email : ")
i= text.find("@")
if i > 0:
    username=text[:i]
    domain=text[i:]
    print(username)
    print(domain)

#فاکتوریل

n = int(input("enter your number : "))
for i in range(1,n+1):
    x = x*i
print(x)