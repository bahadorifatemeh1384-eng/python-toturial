

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
        Book.chap()
        x = int(input("enter a number of book"))
        books.pop(x - 1)




    def cheng():
        Book.chap()
        x = int(input("enter a number of book: "))
      
        t = input("new Title: ")
        s = input("new Subject: ")
        a = input("new Author: ")

        book = books[x-1]
        book.title = t
        book.author = a
        book.subject = s

    def chap():
        # print("title:" + self.title, "author:" + self.author, "subject:" + self.subject )
        for index, book in enumerate(books):
            print(f"{index +1}. Title: {book.title}, Author: {book.author}, Subject: {book.subject}")
       


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





