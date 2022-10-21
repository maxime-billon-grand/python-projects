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


lifes = selectDifficulty()
print(lifes)
