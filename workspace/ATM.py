def birthState(president):

        states = {'Barack Hussein Obama II':'Hawaii',
        'George Walker Bush':'Connecticut',
        'William Jefferson Clinton':'Arkansas',
        'George Herbert Walker Bush':'Massachussetts',
        'Ronald Wilson Reagan':'Illinois',
        'James Earl Carter, Jr':'Georgia'}
  
        
        #You can access the items of a dictionary by referring to its key name, inside square brackets
        return states[president]

        
        
     
     
#reName=input("President Name")

#rint(birthState(PreName))
print("")



def DIV(a,b):
   
    try:
        return a/b
    except ZeroDivisionError:
        print "division by zero!"
  
    
    
z=DIV(4,2)
print(z)


#Define a function which can print a dictionary where the keys are numbers between 
#1 and 3 (both included) and the values are square of keys.

Dict={}

dict[1]=1

