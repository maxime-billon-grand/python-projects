# Tic Tac Toe ou "Jeu du morpion" in french
#
# [[-,-,-]
#  [-,-,-]
#  [-,-,-]]
#


import functions

# ==================== BEGINNING OF FUNCTIONS

def displayMap(m:list):
    print("          =============")
    print("          |", m[0][0], "|", m[0][1], "|", m[0][2], "|")
    print("          |---|---|---|")
    print("          |", m[1][0], "|", m[1][1], "|", m[1][2], "|")
    print("          |---|---|---|")
    print("          |",m[2][0], "|", m[2][1], "|", m[2][2], "|")
    print("          =============")

def checkCoordinates(m:list, l:int, c:int):
    z = False
    while not z:
        if l not in range(3) or c not in range(3):
            print("Invalid coordinates\nCoordinates should be formatted 'a b' with a & b between 0 and 2")
            coord = str(input("Please enter coordinates: "))
            l = int(coord[0])
            c = int(coord[2])
        elif m[l][c] == "-":
            z = True
            return (l, c)
        else:
            print("Invalid coordinates\nThis place is already used")
            coord = str(input("Please enter coordinates: "))
            l = int(coord[0])
            c = int(coord[2])

def userNewGame(user:str):

    with open("./scores.txt", "r+") as f:
        
        t=f.read()
        #print(t)
        listlines=t.split("\n")
        #print(listlines)

        if user in t:
            f.seek(0)
            for line in listlines:
                if user not in line and line != "":
                    f.write(line+"\n")
                elif user in line:
                    victories=line.split(",")[1]
                    nbrMatchs=line.split(",")[2]
                    nbrMatchs=str(int(nbrMatchs)+1)
                    #print("nbrMatchs=",nbrMatchs)

            f.write(user+","+victories+","+nbrMatchs+"\n")
        else:
            f.write(user+",0,1\n")

def userNewVictory(user:str):
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
                    victories=str(int(line.split(",")[1])+1)
                    nbrMatchs=line.split(",")[2]
                    print("nbrMatchs=",nbrMatchs)
                    print("victories=",victories)

            f.write(user+","+victories+","+nbrMatchs+"\n")

def seeScores():
    print(" //===============\\\\")
    print("||   SCORE BOARD   ||")
    print(" \\\\===============//")
    for line in open("./scores.txt", "r"):
        score = line.split(",")
        print(">> Player", score[0], ">> Victories:", score[1],"- Games played:", score[2][:-1])

def checkLines(m:list):
    i=0
    for l in m:
        if m[i][0] == m[i][1] == m[i][2] and m[i][0] != "-":
            return (True, i, m[i][0])
        i+=1
    return (False, None, None)

def checkColumns(m:list):
    i=0
    for c in m:
        if m[0][i] == m[1][i] == m[2][i] and m[0][i] != "-":
            return (True, i, m[0][i])
        i+=1
    return (False, None, None)

def checkDiagonals(m:list):
    if m[0][0] == m[1][1] == m[2][2] and m[0][0] != "-":
        return (True, "\\", m[0][0])
    elif m[0][2] == m[1][1] == m[2][0] and m[0][2] != "-":
        return (True, "/", m[0][2])
    else:
        return (False, None, None)

def checkWinner(m:list, player:str):
    if checkLines(m)[0]:
        print("          +++++++++++++")
        print("          ++ VICTORY ++")
        print("          VVVVVVVVVVVVV")
        displayMap(m)
        print(player, "WON !!", "3 aligned", checkLines(m)[2], "in the line", checkLines(m)[1])
        userNewVictory(player)
        return True
    elif checkColumns(m)[0]:
        print(          "+++++++++++++")
        print("          ++ VICTORY ++")
        print("          VVVVVVVVVVVVV")
        displayMap(m)
        print(player, "WON !!", "3 aligned", checkColumns(m)[2], "in the column", checkColumns(m)[1])
        userNewVictory(player)
        return True
    elif checkDiagonals(m)[0]:
        print("          +++++++++++++")
        print("          ++ VICTORY ++")
        print("          VVVVVVVVVVVVV")
        displayMap(m)
        print(player, "WON !!", "3 aligned", checkDiagonals(m)[2], "in the diagonal", checkDiagonals(m)[1])
        userNewVictory(player)
        return True
    else:
        return False

def initialise():
    matrix = [["-","-","-"],["-","-","-"],["-","-","-"]]
    print("Here's the board :")
    displayMap(matrix)
    user1 = str(input("Player 1 - symbol X - Enter your name: "))
    user1 = functions.upperFirstLetter(user1)
    userNewGame(user1)
    user2 = str(input("Player 2 - symbol O - Enter your name: "))
    user2 = functions.upperFirstLetter(user2)
    userNewGame(user2)
    return (matrix, user1, user2)

def play():
    init=initialise()
    matrix, user1, user2=init[0], init[1], init[2]

    t, winner = 1, False
    while t <= 9 and winner == False :
        if t%2 == 0 :
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print(user2, "it's your turn to play !\nPlace your O")
            displayMap(matrix)
            coordinates = str(input("Enter the two coordinates (between 0 and 2) separated by a space: "))
            l = int(coordinates[0])
            c = int(coordinates[2])
            coordinates = checkCoordinates(matrix, l, c)
            l = coordinates[0]
            c = coordinates[1]
            matrix[l][c] = "O"

            winner = checkWinner(matrix, user2)

        else:
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print(t, user1, "it's your turn to play !\nPlace your X")
            displayMap(matrix)
            coordinates = str(input("Enter the two coordinates (between 0 and 2) separated by a space: "))
            l = int(coordinates[0])
            c = int(coordinates[2])
            coordinates = checkCoordinates(matrix, l, c)
            l = coordinates[0]
            c = coordinates[1]

            matrix[l][c] = "X"

            winner = checkWinner(matrix, user1)

        t+=1
    
    if t == 10:
        print("      :::::::::::::::::::::")
        print("      :::  END OF GAME  :::")
        print("      :::::::::::::::::::::")
        print("      :::   NO WINNER   :::")
        print("      :::::::::::::::::::::")


# ==================== END OF FUNCTIONS



mode = 0

while type(mode) is not int or mode != 1 or mode != 2 :
    mode = input("Do you want to play (1) or see scores (2) ? ")
    if mode == "1":
        print("")
        play()
        break

    elif mode == "2":
        seeScores()
        break

    else:
        print("You didn't enter a valid value")


