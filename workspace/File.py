#refrence to file
f=open("words.txt","r")
# data is a variable that holds all data in words.txt
#readline()  reading line by line
data=f.readli()
List_data=data.split(" ");
# counter to count 'There' word
counter=0
for index in range(len(List_data)):
    if  List_data[index]=='There':
       counter=counter+1
      

print(counter)
f.close()