import random
import functions

# Asking the difficulty until a valid value is entered, define the number of lifes
def selectDifficulty():
    difficulty=0
    while type(difficulty) is not int or difficulty not in range(1,4) :
        difficulty = input("In which difficulty do you want to play ?\n 1 - Easy mode\n 2 - Middle mode\n 3 - Hardcore mode\n")
        if difficulty == "1":
            lifes=10
            break
        elif difficulty == "2":
            lifes=7
            break
        elif difficulty == "3":
            lifes=4
            break
        else:
            print("You didn't enter a valid value")
    
    return lifes

# Message if win
def winMessage():
    print("      :::::::::::::::::::::")
    print("      :: CONGRATULATIONS ::")
    print("      :::::::::::::::::::::")
    print("      :::    YOU WIN    :::")
    print("      :::::::::::::::::::::")

# Message if game over
def looseMessage():
    print("      ||________________")
    print("      ||  /            |")
    print("      || /             O")
    print("      ||/             /|\\")
    print("      ||              / \\")
    print("      ||")
    print("      =====================")
    print("      :::::::::::::::::::::")
    print("      :::   GAME OVER   :::")
    print("      :::   YOU LOOSE   :::")
    print("      :::::::::::::::::::::")

# Open the file dico_france.txt, put the lines in a list, then choose one randomly, remove accents, put in lowercase
def defineWord():
    file=open("./dico_france.txt","r")
    lines=file.readlines()
    word = random.choice(lines)
    word = functions.removeAccents(word)[:-1]
    word = functions.myLower(word)
    file.close()

    return word

# Print a list as a string
def printList(l:list):
    s=""
    spaces="     "
    for e in l:
        s += e
    print(spaces,"-"*(len(s)+4))
    print(spaces,"|",functions.myUpper(s),"|")
    print(spaces,"-"*(len(s)+4))

# Define the string of underscores but keeping the -, spaces, ', 
def defineUnderscores(w:str):
    s=""
    for letter in w:
        match letter:
            case "-":
                s += letter
            case " ":
                s += letter
            case "'":
                s += letter
            case "!":
                s += letter
            case _:
                s += "_"
    return s


# Initialise and select difficulty
totalLifes = selectDifficulty()
life = totalLifes
word = defineWord()
found = defineUnderscores(word)
foundList = list(found)


# Uncomment theses lines to debug
#print(word)
#print (found)
#print(foundList)
printList(foundList)
while life != 0 and "_" in foundList:
    letter = str(input("Please enter a letter : "))
    letter = functions.myLower(letter)
    if letter in word:
        print("Nice ! You found a letter")
        i=0
        for l in word:
            if letter == l:
                foundList[i] = letter
            i+=1
        printList(foundList)
    else:
        life -= 1
        print("Oh crap ! This letter is not in the word ")
        print("You have", life, "lives left")
        printList(foundList)

# Message if all lives are consummed
if life == 0:
    looseMessage()
elif "_" not in foundList:
    winMessage()

