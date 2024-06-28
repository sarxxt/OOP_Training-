class Person:
    def __init__(self, name, age):  ##All classes have a function called __init__(), which is always executed when the class is being initiated.
        self.name=name 
        self.age = age 

p1=Person("sara",21)

print(p1.name)
print(p1.age)