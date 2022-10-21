# This function create a substitute to the string.index() method
def searchLetterInList(letter:str, list:list):
    i,j = 0,0
    for l in list:
        if l == letter:
            j=i  
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

#==============Function CAPTIALIZE======================
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

#==============Remove accents and special caracteres
def removeAccents(s:str):
    accents=["é","è","ê","à","â","ç","î","ù","û","Â","É","È","Ç","œ"]
    withoutaccents=["e","e","e","a","a","c","i","u","u","A","E","E","C","oe"]
    l = list(s)                         # Place str in a list
    j=0
    for letter in s:
    
        if letter in accents:
            i = searchLetterInList(letter, accents)
            l[j] = withoutaccents[i]
        j+=1

    s2 = ""
    for e in l:                         # Recreate the str from the list
        s2 += e
    return s2

