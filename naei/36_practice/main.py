

class Book :

    def __init__(self, title, author, subject ):
        self.title = title
        self.author = author
        self.subject = subject

    def add():
        t = input("Title: ")
        s = input("Subject: ")
        a = input("Author: ")
        book = Book(t, s, a)
        books.append(book)

    def remove():
        x = input("enter a number of book")
        books.remove(x)




    def cheng():
        pass

    def chap():
        # print("title:" + self.title, "author:" + self.author, "subject:" + self.subject )
        print(books)
       

# book1 = Book("rrrrrr", "tttttt", "kkkkkkkkkk")
# book1.chap()
books = []
while 1:
    i = input("1.add \n2.remove \n3.cheng\n4.list\n")
    if i == "0":
        break
    elif i == "1":
        Book.add()
    elif i == "2":
        Book.remove()
    elif i == "3":
        Book.cheng()
    elif i == "4":
       Book.chap()





