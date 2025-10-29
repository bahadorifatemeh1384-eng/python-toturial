class User:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password 
        self.email = email

    def print1():
        for index, user in enumerate(users):
            print(f"{index +1}. username: {user.username}, password: {user.password}, email: {user.email}")
            print("isGmail: ","yes" if User.is_gmail() else "no")

    def print2(self):
        print(self.username, self.email)


    def is_gmail():
        return user.email.endswith("@gmail.com")
    

users = []
while 1:
    u = input("username: " )
    if u == "0" : break
    p = input("password: ")
    e = input("email: ")

    user = User(u, p, e)
    users.append(user)

print("All Users : " , len(users))
User.print1()
