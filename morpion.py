# Tic Tac Toe ou "Jeu du morpion" in french
#
# [[-,-,-],
#  [-,-,-],
#  [-,-,-]]
#


import functions

# ==================== BEGINNING OF FUNCTIONS

# Function displaying the tic tac toe board
def displayMap(m:list):
    print("          =============")
    print("          |", m[0][0], "|", m[0][1], "|", m[0][2], "|")
    print("          |---|---|---|")
    print("          |", m[1][0], "|", m[1][1], "|", m[1][2], "|")
    print("          |---|---|---|")
    print("          |",m[2][0], "|", m[2][1], "|", m[2][2], "|")
    print("          =============")

# Function asking and checking if coordinates are valides
def askCoordinates(m:list):
    while True:
        coord = str(input("Enter the two coordinates (between 0 and 2) separated by a space: "))

        # Checking if coordinates have correct format
        if len(coord) == 3 :
            l = int(coord[0])
            c = int(coord[2])

            # Checking if coordinates aren't outside the board
            if l in range(3) and c in range(3):

                # Checking if coordinates don't target an already used place
                if m[l][c] == "-":
                    return (l, c)
                else:
                    print("Invalid coordinates\nThe coordinates you entered are already used !")
            else:
                print("Invalid coordinates\nThe coordinates should be between 0 and 2 !")
        else:
            print("Invalid coordinates\nCoordinates should be formatted 'a b' with a & b between 0 and 2")

# Function incrementing in the score.txt the number of parties played
def userNewGame(user:str):

    # Opening the file in modification mode
    with open("./scores.txt", "r+") as f:
        
        # Read the file and put lines in a list
        t=f.read()
#        print(t)
        listlines=t.split("\n")
#        print(listlines)

        # If user exists in the file
        if user in t:
            # Go to beginning of file
            f.seek(0)

            # Open list to have one line at a time
            for line in listlines:
                # Re-write in file the lines that does not contains user
                if user not in line and line != "":
                    f.write(line+"\n")
                
                # In the line that contains user, split it in a list,
                # and put number of victories and number of games played in variables that can be incremented
                elif user in line:
                    victories=line.split(",")[1]
                    nbrMatchs=line.split(",")[2]
                    # Increment number of games played
                    nbrMatchs=str(int(nbrMatchs)+1)
#                    print("nbrMatchs=",nbrMatchs)

            # Re-put in one big string, and re-write it in the file
            f.write(user+","+victories+","+nbrMatchs+"\n")

        # If user does not exist in the file, just add a line with 0 victories and 1 game played
        else:
            f.write(user+",0,1\n")

# Function incrementing in the score.txt the number of victories
def userNewVictory(user:str):

    # Opening the file in modification mode
    with open("./scores.txt", "r+") as f:
        
        # Read the file and put lines in a list
        t=f.read()
#        print(t)
        listlines=t.split("\n")
#        print(listlines)

        # If user exists in the file
        if user in t:
            # Go to beginning of file
            f.seek(0)

            # Open list to have one line at a time
            for line in listlines:
                # Re-write in file the lines that does not contains user
                if user not in line and line != "":
                    f.write(line+"\n")
                # In the line that contains user, split it in a list,
                # and put number of victories and number of games played in variables that can be incremented
                elif user in line:
                    # Increment number of victories
                    victories=str(int(line.split(",")[1])+1)
                    nbrMatchs=line.split(",")[2]
                    print("nbrMatchs=",nbrMatchs)
                    print("victories=",victories)

            # Re-put in one big string, and re-write it in the file
            f.write(user+","+victories+","+nbrMatchs+"\n")

# Function displaying the scores with some formatting
def seeScores():
    print(" //===============\\\\")
    print("||   SCORE BOARD   ||")
    print(" \\\\===============//")
    for line in open("./scores.txt", "r"):
        score = line.split(",")
        print(">> Player", score[0], ">> Victories:", score[1],"- Games played:", score[2][:-1])

# Function checking if there is a victory on the lines
# Return a tuple with victory = True, number of the line, and the winner symbol
def checkLines(m:list):
    i=0
    for l in m:
        if m[i][0] == m[i][1] == m[i][2] and m[i][0] != "-":
            return (True, i, m[i][0])
        i+=1
    return (False, None, None)

# Function checking if there is a victory on the columns
# Return a tuple with victory = True, number of column, and the winner symbol
def checkColumns(m:list):
    i=0
    for c in m:
        if m[0][i] == m[1][i] == m[2][i] and m[0][i] != "-":
            return (True, i, m[0][i])
        i+=1
    return (False, None, None)

# Function checking if there is a victory on the diagonals
# Return a tuple with victory = True, diagonal, and the winner symbol
def checkDiagonals(m:list):
    if m[0][0] == m[1][1] == m[2][2] and m[0][0] != "-":
        return (True, "\\", m[0][0])#
    elif m[0][2] == m[1][1] == m[2][0] and m[0][2] != "-":
        return (True, "/", m[0][2])
    else:
        return (False, None, None)

# Function checking if there is a victory
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

# Intialising the game, and return the matrix and the players 
def initialise():
    # Matrix
    matrix = [["-","-","-"],["-","-","-"],["-","-","-"]]
    print("Here's the board :")
    displayMap(matrix)

    # Player 1
    user1 = str(input("Player 1 - symbol X - Enter your name: "))
    user1 = functions.upperFirstLetter(user1)
    userNewGame(user1)

    # Player 2
    user2 = str(input("Player 2 - symbol O - Enter your name: "))
    user2 = functions.upperFirstLetter(user2)
    userNewGame(user2)

    return (matrix, user1, user2)

# Main fonction of the game
def play():
    # Initialisation and 
    init=initialise()
    matrix, user1, user2=init[0], init[1], init[2]

    # Declaration of the variables conditions of the main loop, number of round, and winner (boolean, is there a winner ?) 
    round, winner = 1, False
    # Each round the player change, and the game stop if there is a winner, or if all 9 round are completed
    while round <= 9 and winner == False :
        if round % 2 == 0 :
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print(user2, "it's your turn to play !\nPlace your symbol - O")
            displayMap(matrix)

            coordinates = askCoordinates(matrix, l, c)
            l = coordinates[0]
            c = coordinates[1]

            matrix[l][c] = "O"

            winner = checkWinner(matrix, user2)

        else:
            print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print(user1, "it's your turn to play !\nPlace your symbol - X")
            displayMap(matrix)
            coordinates = askCoordinates(matrix, l, c)
            l = coordinates[0]
            c = coordinates[1]

            matrix[l][c] = "X"

            winner = checkWinner(matrix, user1)

        round +=1
    
    # Message if end game
    if round == 10:
        print("      :::::::::::::::::::::")
        print("      :::  END OF GAME  :::")
        print("      :::::::::::::::::::::")
        print("      :::   NO WINNER   :::")
        print("      :::::::::::::::::::::")
        displayMap(matrix)


# ==================== END OF FUNCTIONS



mode = 0
# Asking choice of user, play or see score board ?
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


