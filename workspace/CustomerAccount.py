import  datetime
import argparse



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
     
     
    
    
        

 # Create  a parser object
parser = argparse.ArgumentParser()
parser.add_argument('FullName', type=str, help='Type full nale')
parser.add_argument('ssn', type=str, help='Type full nale')
 
args = parser.parse_args()         
C1=CustomerAccount(args.FullName,args.ssn)



