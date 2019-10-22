#(Initail point, end point,step) ,2 parameter optional (endPoint), 1 Required

#Range generate a sequence of number

#List can store multiple value

country_list = ["USA", "Canada", "Thailand", "Denmark", "Japan"]
# check if Japan is in the  country_list ,
# inorder to access a list list_name[]
#x=input("Enter a country!")
'''
x='Japan'
country_list = ["USA", "Canada", "Thailand", "Denmark", "Japan"]
for i in range(len(country_list)):
    if  x not in country_list:
            print("Try again!") 
            break
    
    else:
        if  country_list [i]==x:
            print("Boom",country_list[i])
            
'''
'''
Write A python statements  that accepts a number N  and returns   N, N-1...........1

input

5

output 

12345

Read a number N   using input()
 '''   
 
def My_func(value):
   sum=0
   for i in range(value+1):   #  0 1 2 3 4 5 6 7 8 9 10
       sum=i+sum
   return sum

x=10
#call the function
#assign the returned value from  My_func(value) to var called Fun_res
Fun_res=My_func(10)
print(Fun_res)



def Sum_list(list):
    toltal=0
    #loop :
        #add elements
    return  toltal
    


List=[2,4,5,6,7]
Sum_list(List)





