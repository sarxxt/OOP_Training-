class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    

# use super() to call the .speak() method of the 
# parent class with the same argument passed to sound as 
# the GoldenRetriever class’s .speak() method.


class GoldenRetriever (Dog): 
    def speak(self, sound ="Bark"):  
        return super().speak(sound)


buddy = GoldenRetriever("Buddy", 9)
print(buddy)
print(buddy.speak())
