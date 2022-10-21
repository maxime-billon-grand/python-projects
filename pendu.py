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
    for e in l:
        s += e
    print(":"*)
    print(s)


# Initialise and select difficulty
totalLifes = selectDifficulty()
lifes = totalLifes
word = defineWord()
found = "_"*len(word)
foundList = list(found)

#print(word)


while lifes != 0 and "_" in foundList:
    letter = str(input("Please enter a letter : "))
    letter = functions.myLower(letter)
    if letter in word:
        print("Gagné")
        i=0
        for l in word:
            if letter == l:
                foundList[i] = letter
            i+=1
        printList(foundList)
    else:
        lifes -= 1
        print("Perdu")
        printList(foundList)
