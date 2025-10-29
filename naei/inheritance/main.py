class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def jam(self):
        return self.x + self.y

    def tafrigh(self):
        return self.x - self.y
    
    def zarb(self):
        return self.x * self.y
    
    def taghsim(self):
        return self.x / self.y
    

num = Calculator(2 ,3);
print (num.jam())
print (num.tafrigh())
print (num.zarb())
print (num.taghsim())