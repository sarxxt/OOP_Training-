class Person:
    def __init__(self, fname, lname):
        self.first_name =fname
        self.last_name =lname

    def printname(self):
        print("my name is: " + self.first_name + self.last_name)


class Student(Person):
    pass

s1= Student("sara", "rasool")
s1.printname()        