
class Insurance:
    
    #__init  Built-in function 
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def Calculate_Ins(self):
        base=1000
        if self.age ==16 or self.age <=19:
            Totol=base+(base*0.15)
            print(self.name+" "+str(self.age)+"  "+str(Totol)) 
        elif self.age ==20 or self.age <=25:
           Totol=base+(base*0.05)
           print(self.name+" "+str(self.age)+"  "+str(Totol)) 
        elif self.age >=25:
           Totol=base-(base*0.1)
           print(self.name+" "+str(self.age)+"  "+str(Totol)) 
        else:
                print(self.name+" "+str(self.age)+"No Insurance")     
        
        
    
    def display(self):
        print (self.name,self.age)
        
    
      

f=open("data.txt","r")
for line in f:
         i=1
         P="P"+str(1)
         data=line.split(",")
         P=Insurance(data[0],int(data[1]))
         i=i+1
         P.Calculate_Ins()
         
         
f.close()


'''
#print(data)
         obj="P"+str(i)
         i=i+1
         #listof_custoners.append(data)
         obj=Insurance(data[0],int(data[1]))
         obj.check()
print(listof_custoners)
for i in range(len(listof_custoners)):
    obj="P"+str(i)
    #obj=Insurance(List_data[i],int(List_data[i+1]))
    #print(obj.check())
'''