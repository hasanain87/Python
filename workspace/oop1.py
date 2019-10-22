#Object For instance, an object could represent a person with a name property, age, address, etc.
#the class is the blueprint, an instance is a copy of the class with actual values, 


class Car:
    # class Attributes,features of an object
    #shared for all instances eg. cars
    axles = 2
    wheels = 4

    
    
    
    #se the __init__() function to assign (initialize)values to object properties,
    #self is a reference to the class instance itself
    # each car has a  unique attributes  like make, model.....
    def __init__(self, make, model, price, inventory):
        self.make = make
        self.model= model
        self.price = price
        self.inventory = inventory

    
    
    #is bound to a class rather than its object.,
    # attached to a class by first parameter cls
    @classmethod
    def calcMPG(cls, miles, gallons):
        return miles / gallons
        
        
        
    def display(self):
        print("make "+self.make,"model "+self.model,self.price,self.inventory)
    
    
    
    #Python has no way to determine what the greater-than operation means when working with the Object
  #class objects,Comparision methods
  #Defines behavior for the greater-than operator, 
  #implements behavior for >
    def __gt__ (self,other):
        if self.inventory>other.inventory:
            return True

   
   
    
    
    
    def __sub__(self, other):
       return self.price - other.price
    
    
    
    
# new, unique instance of a class
# create a new instance and  assign it to var car1
# init get called every time you craete new obj
#To use a class, you have to instantiate it

car1 = Car("Chevy", "Volt", 150000.00, 10)
car2 = Car("Ford", "Focus", 10000.00, 20)


#car1.display()
#print("car1.axles",car1.axles,)


#print("How many Miles per galon?",Car.calcMPG(120, 3.3))

# you must defined gt method 
if (car2 > car1):
         print("Chevy  Has larger Inv.than Ford ")

 #print( car1 - car2)
