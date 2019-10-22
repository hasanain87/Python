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

    
    
    #use outside of class instances,functions that are independent of any instance data.
    @classmethod
    def calcMPG(cls, miles, gallons):
        return miles / gallons
        
    def display(self):
        print("make "+self.make,"model "+self.model,self.price,self.inventory)
    
    
#Sedan (inherits) all of the original attributes and methods of
#the superclass, plus adds its own attributes and methods specific to the subclass  

#class car is  specified  as  the supercalss (parent) for the sedan class
class Sedan(Car):
    def __init__(self, make, model, price, inventory, doors, seats):
        #refers to the constructor for the Car class (parent)
        Car.__init__(self,make, model, price, inventory)
        #super(Sedan, self).__init__(make, model, price, inventory)
        
        self.doors = doors
        self.seats = seats
        
        
    
    def display(self):
        print("doors",self.doors,"make "+self.make,"model "+self.model,self.price,self.inventory)
      

sedan1 = Sedan("Ford", "Focus", 10000.00, 5, 4, 5)   
sedan1.display()