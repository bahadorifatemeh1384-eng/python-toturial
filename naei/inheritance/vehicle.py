class Vehicle:

    def __init__(self, model, color,):
        
        self.model = model
        self.color = color


    def get_info(self):

        return f"Model: {self.model}, Color: {self.color}"


class Car(Vehicle):

    def __init__(self, model, color, num_of_wheel):
        super().__init__(model, color)
        self.num_of_wheel = num_of_wheel

    def get_info(self):

        return f"Model: {self.model}, Color: {self.color}, Number of wheels: {self.num_of_wheel}"
    

model = input("enter model: ")
color = input("enter color: ")
num_of_wheels = input("enter enter number of wheels: ")
        
if num_of_wheels == "":
    c1 = Vehicle(model, color)
else:
    c1 = Car(model, color, num_of_wheels)


print(c1.get_info())