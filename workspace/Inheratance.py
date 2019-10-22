from random import *
import  datetime

#class Person base class Parents
class Person:
    
    def __init__ (self,Fullname,gender,DoB ):
        self.S_DoB=DoB
        self.S_Fullname=Fullname
        self.S_gender=gender
      
    

#class school Child subclass
class school (Person):
    #Constructor for school class (child)
    def __init__ (self,Fullname,gender,DoB,list_grade ):
        # call __init__ for the Person as a parent class 
      Person.__init__(self,Fullname,gender,DoB)
      
      self.S_SID=self.SID_Generator()
      self.start_Sem=str(datetime.datetime.now().date())
      self.grade=list_grade
      
      
    def Display(self):
        print(self.S_Fullname,self.S_SID,self.S_gender,self.S_DoB,self.start_Sem,self.grade)
    
    def SID_Generator(self):
        random1=randint(40,70)
        random2=randint(80,99)
        return str(15)+str(random1)+str(random2)
       
       
    
        
S1=school("Leza Smith","F","09-1999",{'MAth':"A","Bio":"C"})
S1.Display()























"""class Person:  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
   
  
    def showAge(self):  
        print(self.age)  
  
    #end of class definition  
  
# defining another class  
class Student(Person): # Person is the  
    def __init__(self, personName,personAge,studentId): 
        Person.__init__(self,personName,personAge)
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId
        
    def showName(self):  
        print(self.name,self.age)  
  
  
  
# Create an object of the subclass  
Student1 =Student ('John', 30, '102')  
Student1.showName()  
print(Student1.getId())  
"""