class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("my name is: " + self.name)

p1 =Person("Sara", 21)
p1.myfunc()

## MOdifying object properties
p1.name = "hamza"
p1.myfunc()

## you can delete object properties
del p1.age 

## you can delete object too
del p1

