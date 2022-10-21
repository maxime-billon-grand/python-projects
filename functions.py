# This function create a substitute to the string.index() method
def searchLetterInList(letter:str, list:list):
    i,j = 0,0
    for l in list:
        if l == letter:
            j=i
            i+=1  
        i+=1
    return j

#==============Function UPPER======================
def myUpper(s:str):
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Ç","À","É","È"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç","à","é","è"]

    l = list(s)                         # Place str in a list
    j=0
    for letter in l:
        if letter in lower:
            i = searchLetterInList(letter, lower)
            l[j] = upper[i]
        j+=1

    s2 = ""
    for e in l:                         # Recreate the str from the list
        s2 += e
    return s2

#==============Function LOWER======================
def myLower(s:str):
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Ç","À","É","È"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç","à","é","è"]

    l = list(s)                         # Place str in a list
    j=0
    for letter in s:
        if letter in upper:
            i=searchLetterInList(letter, upper)
            l[j] = lower[i]
        j+=1
    s2 = ""
    for e in l:                         # Recreate the str from the list
        s2 += e                     
    return s2

def upperFirstLetter(s:str):
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Ç","À","É","È"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç","à","é","è"]
    sep=[" ", ",", ".", ";", "-"]

    l = list(s)                 # Place str in a list
# Replace the first character & the first character after space by the uppercase
    i = 0
    while i+1 <= len(l):
        if (i == 0 or l[i-1] in sep) and l[i] in lower:
            l[i]=myUpper[l[i]]
        elif i > 0:
            l[i]=myLower(l[i])

        i+=1

    s2 = ""
    for e in l:                         # Recreate the str from the list
        s2 += e
    return s2  

def checkUser(user:str):

    with open("./scores.txt", "r+") as f:
        
        t=f.read()
        print(t)
        listlines=t.split("\n")
        print(listlines)


        if user in t:
            f.seek(0)
            for line in listlines:
                if user not in line and line != "":
                    f.write(line+"\n")
                elif user in line:
                    victories=line.split(",")[1]
                    nbrMatchs=line.split(",")[2]
                    nbrMatchs=str(int(nbrMatchs)+1)
                    print("nbrMatchs=",nbrMatchs)

            f.write(user+","+victories+","+nbrMatchs+"\n")
        else:
            f.write(user+",0,1\n")
        
    
