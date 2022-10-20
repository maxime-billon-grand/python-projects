# Tic Tac Toe ou "Jeu du morpion" in french
#
# [[-,-,-]
#  [-,-,-]
#  [-,-,-]]
#
#
#



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

def seeScores():
    c1, c2, c3 ="", "", ""
    for line in open("./scores.txt", "r"):
        print(line)

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
        print("+++++++++++++")
        print("++ VICTORY ++")
        print("+++++++++++++")
        print(player, "WON !!", "3 aligned", checkLines(m)[2], "in the line", checkLines(m)[1])
        return True
    elif checkColumns(m)[0]:
        print("+++++++++++++")
        print("++ VICTORY ++")
        print("+++++++++++++")
        displayMap(m)
        print(player, "WON !!", "3 aligned", checkColumns(m)[2], "in the column", checkColumns(m)[1])
        return True
    elif checkDiagonals(m)[0]:
        print("+++++++++++++")
        print("++ VICTORY ++")
        print("+++++++++++++")
        displayMap(m)
        print(player, "WON !!", "3 aligned", checkDiagonals(m)[2], "in the diagonal", checkDiagonals(m)[1])
        return True
    else:
        return False

def play():
    matrix = [["-","-","-"],["-","-","-"],["-","-","-"]]
    print("Here's the plateau :")
    displayMap(matrix)
    user1 = str(input("Player 1 - symbol X - Enter your name: "))
    user2 = str(input("Player 2 - symbol O - Enter your name: "))

    # Write in the score.txt if new player or gamesplayed+=1 if player already known

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
            print(user1, "it's your turn to play !\nPlace your X")
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




mode = int(input("Do you want to play (1) or see scores (2) ? "))


match mode:
    case 1:
        print("play")
        play()

    case 2:
        print("see scores")
        seeScores()
    case _:
        # SEE THE LOOP TO ASK
        mode = int(input("You didn't enter a valid value\nDo you want to play (1) or see scores (2) ? "))


