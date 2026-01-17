# single or basic inheritance.

#base class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, I am {self.name} from Parent class.")
# #derived class
# class Child(Parent):
#     # def __init__(self, name, age):
#     #     super().__init__(name)  # calling the constructor of the base class
#     #     self.age = age
#     def play(self):
#         print(f"{self.name} is playing from Child class.")

#     # def introduce(self):
#     #     print(f"Hello, I am {self.name} and I am {self.age} years old from Child class.")
# # Creating an object of the derived class
# child = Child("Alice")  
# child.greet()  # Output: Hello, I am Alice from Parent class.
# child.play()   # Output: Alice is playing from Child class. 


#--------------------------------------------------------
# multilevel inheritance example

# #base class
# class Grandparent:
#     def __init__(self, family_name):
#         self.family_name = family_name

#     def tell_story(self):
#         print(f"{self.family_name} family story from Grandparent class.")

# #intermediate derived class
# class Parent(Grandparent):
#     def work(self):
#         print(f"{self.family_name} parent is working from Parent class.")

# #derived class
# class Child(Parent):
#     def play(self):
#         print(f"{self.family_name} child is playing from Child class.")

# # Creating an object of the most derived class
# child = Child("Smith")
# child.tell_story()  # Output: Smith family story from Grandparent class.
# child.work()        # Output: Smith parent is working from Parent class.
# child.play()        # Output: Smith child is playing from Child class.
#--------------------------------------------------------

# hierarchical inheritance example
# #base class
# class parent:
#     def __init__(self, family_name):
#         self.family_name = family_name

#     def family_info(self):
#         print(f"{self.family_name} family info from Parent class.")
# #derived class 1
# class child1(parent):
#     def play(self):
#         print(f"{self.family_name} child1 is playing from Child1 class.")
# #derived class 2
# class child2(parent):
#     def study(self):
#         print(f"{self.family_name} child2 is studying from Child2 class.")  
# # Creating objects of the derived classes
# child1 = child1("Johnson")
# child1.family_info()  # Output: Johnson family info from Parent class.
# child1.play()         # Output: Johnson child1 is playing from Child1 class.
# child2 = child2("Johnson")
# child2.family_info()  # Output: Johnson family info from Parent class.
# child2.study()        # Output: Johnson child2 is studying from Child2 class.
#--------------------------------------------------------
# multiple inheritance diamond problem example
# 
# #base class 
class A:
    def __init__(self, name):
        self.value = name
    
    def greet(self):
        print(f"Hello from class A, value: {self.value}")

# inherited class 1
class B(A):

    def greet(self):
        print(f"Hello from class B, value: {self.value}")
        super().greet()
# inherited class 2
class C(A):

    def greet(self):
        print(f"Hello from class C, value: {self.value}")
        super().greet()
# derived class
class D(B, C):
    def greet(self):
        print(f"Hello from class D, value: {self.value}")
        super().greet()

# Creating an object of the derived class
d = D("Diamond")
d.greet()
# Output:
# Hello from class D, value: Diamond    

# hybrid inheritance example

# Base class
class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# intermediate class 1 (hierarchy 1)
class mammal(animal):
    def walk(self):
        print(f"{self.name} walks on land")

# intermediate class 2 (hierarchy 2)
class bird(animal):
    def fly(self):
        print(f"{self.name} flies in the sky")

# derived class
class bat(mammal, bird):
    def __init__(self, name):
       mammal.__init__(self, name)   #explicitly calling mammal's constructor

    def nocturnal_activity(self):
        print(f"{self.name} is active at night")

# Creating an object of the derived class
bat_instance = bat("Batty")
bat_instance.speak()               # From animal class  
bat_instance.walk()                # From mammal class
bat_instance.fly()                 # From bird class
bat_instance.nocturnal_activity()  # From bat class
# Output:
# Batty makes a sound
# Batty walks on land
# Batty flies in the sky        

