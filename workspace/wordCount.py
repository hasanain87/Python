#an 

'''
COMMON_WORDS = {"the", "be", "are", "is", "were", "was", "am",
                "been", "being", "to", "of", "and", "a", "in",
                "that", "have", "had", "has", "having", "for",
                "not", "on", "with", "as", "do", "does", "did",
                "doing", "done", "at", "but", "by", "from"}*/
 '''
 
COMMON_WORDS = {"the", "be", "are", "is", "were", "was", "am"}
word_count = {}



try:
        f=open("wor.txt","r") 
                #hat reads the whole file at once
        text=f.read()
        all=text.split()
        
except IOError:
        print ("Error: can\'t find file or read data")
        
        
        
    
print(all)
         
for word in all:
             
    if word in COMMON_WORDS:
                    
        if word in word_count:
            word_count[word] += 1          
        else:
                word_count[word] = 1
                             
print(word_count)
             
