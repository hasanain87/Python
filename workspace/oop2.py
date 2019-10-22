class Person:
    
    #__init  Built-in function 
    def __init__(self,name,age,Num,DOB):
      
        self.Fullname=name
        self.age=age
        self.
        self.DOB=DOB

        
    
    def display(self):
        print (self.Fullname,self.age,self.SSN)
        
        
        
    def Background_check(self):
        if self.Fullname=='Leza jackson' and self.SSN=='222-22-2222':
            # has issue 
            print("ah oops unqulified call 911 ")
        else:
            print("qulified")
            
 
        
        
    
    
      
obj1= Person("John Doe", 36,"111-11-1111","02/08/1990")
obj2= Person("Leza jackson",40,"333-23-6578","02/08/1980")
obj3= Person("Robert Smith ",70,"111-31-9456","02/08/1980")
#obj1.display()
#obj2.display()
#obj1.Background_check()
