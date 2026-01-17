# simple inheritance example

## Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


## Derived class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

# Creating objects of the classes
# animal = Animal("Generic Animal")
# animal.speak() # Output: Generic Animal makes a sound

# Creating an object of the derived class
# dog = Dog("Buddy")
# dog.speak()    # Output: Buddy barks



#super keyword example

#super

#base class

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

#derived class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # calling the constructor of the base class
        self.color = color

    def speak(self):
        super().speak()  # calling the method of the base class
        print(f"{self.name}, the {self.color} cat meows")

# Creating an object of the derived class
cat = Cat("Whiskers", "black")
cat.speak()  # Output: Whiskers, the black cat meows