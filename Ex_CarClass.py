class Car:
    def __init__(self, color, milage):
        self.color = color
        self.milage = milage

    def __str__(self):
        return f"The {self.color} has {self.milage: ,} miles"
    
car1 = Car("blue", 20000)
car2 =Car("red", 30000)
print(car1)
print(car2)