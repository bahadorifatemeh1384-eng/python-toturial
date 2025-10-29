class Date:

    def __init__(self, year, month, day):
        self.day = day
        self.month = month
        self.year = year

    def ezafe(self):
        pass


    def kam(self):
        pass


    def show(self):
        return f"day : {self.day} month: {self.month} year: {self.year}"
    


date = input("tarikh :")

year = int(date[:4])
month = int(date[5:7])
day = int(date[8:])

d = Date(year, month, day)



