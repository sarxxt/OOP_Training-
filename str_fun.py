class Person:
    def __init__(self, name, age): #  The self parameter is a 
        self.name = name           #  reference to the current instance of the class, and is used to access variables that belong to the class.
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
p1=Person("sara", 221)
print(p1)    
