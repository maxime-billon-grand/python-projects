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
        return (True, "1", m[0][0])
    elif m[0][2] == m[1][1] == m[2][0] and m[0][2] != "-":
        return (True, "2", m[0][2])
    else:
        return (False, None, None)

def checkWinner(m:list, player:str):
    if checkLines(m)[0]:
        print(player, "WON !!", "3 aligned", checkLines(m)[2], "in the line", checkLines(m)[1])
        return True
    elif checkColumns(m)[0]:
        print(player, "WON !!", "3 aligned", checkColumns(m)[2], "in the column", checkColumns(m)[1])
        return True
    elif checkDiagonals(m)[0]:
        print(player, "WON !!", "3 aligned", checkDiagonals(m)[2], "in the diagonal", checkDiagonals(m)[1])
        return True
    else:
        return False

def displayMap(m:list):
    print("|============")
    print("|", m[0][0], "|", m[0][1], "|", m[0][2], "|")
    print("|===========|")
    print("|", m[1][0], "|", m[1][1], "|", m[1][2], "|")
    print("|===========|")
    print("|",m[2][0], "|", m[2][1], "|", m[2][2], "|")
    print("============|")