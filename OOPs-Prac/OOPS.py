class employee:
    def __init__ (self):

        print("Started executing attributes/data")
        print(id(self))
        #attributes of the class
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")
        # methods of the class
    def travel( self):
        print("this travel method is called manually")
        print(f"Employee is travelling delhi")

    



#create an obj/instance of the class
sam = employee()
print(id(sam))
#calling the method
sam.travel()

# print(type(sam))