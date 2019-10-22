import  datetime




class CustomerAccount():
    
    def __init__(self,FullName,SSN):
        self.FullName=FullName
        self.balance=25.0
        self.SSN=SSN
        self.Store_Obj( self.FullName,self.balance)
        
        
    def Print(self):
        print(self.FullName,self.balance)
        
    
    def deposit(self,newDepo):
        self.balance +=newDepo
        return self.balance
        
        
    def Background_check(self,):
        if self.FullName =="Regi smith" and self.SSN=="88888-288-4444":
            print("We can not open an Account for"+self.FullName)
      
     
    def Withdraw(self,amount):
        if self.balance < amount:
            raise RuntimeError('amount exceed your balance')
        
        self.balance -=amount
        self.Store_Obj(self.FullName,self.balance)
     
        
    def Store_Obj(self,FullName,balance):
        f=open(FullName+".txt","a")
        f.write("Customer name ===  "+FullName+"    Customer balance === "+str(balance)+"    Time === "+str(datetime.datetime.now()))
        f.write("\n")
     
     
    
    
        
    
    
    
    
    
    
      
  
  
  
  
    
        

C1=CustomerAccount("Robert Jack","1111-22-4444")
#newBalance=C1.deposit(float(input("How much ===?")))
C1.Withdraw(10)
#print(newBalance)
C2=CustomerAccount("Albert Nelson","3333-22-4444")
#C3=CustomerAccount("Regi smith","88888-288-4444")

#C3.Background_check()
#C1.Print()

'''
 
    def store_object(self,FullName,balance):
        f=open("customer.txt","a")
        #f.write("appended text")
        f.write(self.FullName+str(self.balance))
        f.write("\n")
        f.close()
    #self.store_object(self.FullName,self.balance)
'''