# game file for streamlit w/o input, while loops, and printing

def set(chosen):
    array = []
    rows = chosen["rows"]
    cols = chosen["cols"]

    S_row = chosen["S"][0]
    S_col = chosen["S"][1]

    E_row = chosen["E"][0]
    E_col = chosen["E"][1]

    X_pos = chosen["X"]
    T_pos = chosen["T"]

    for _ in range(rows):
        array.append([1] * cols)

    for x in X_pos:
        row = x[0]
        col = x[1]
        array[row][col] = 0

    for x in T_pos:
        row = x[0]
        col = x[1]
        array[row][col] = "T"

    array[S_row][S_col] = "S"
    array[E_row][E_col] = "E"

    return array

def canmove(row,col,array):
    totrows = len(array)
    totcols = len(array[0])
    if row < 0 or row >= totrows or col < 0 or col >= totcols:
        return False
    if array[row][col] == 0:
        return False
    return True

def move(Player_row, Player_col, x, array): #x is input.
    
    nrow = Player_row
    ncol = Player_col

    x = x.lower()

    if x == "w":
        nrow -=1
    elif x == "s":
        nrow += 1
    elif x == "a":
        ncol -=1
    elif x == "d":
        ncol += 1
    elif x == "wd" or x == "dw":
        nrow -=1
        ncol +=1
    elif x == "sd" or x == "ds":
        nrow += 1
        ncol += 1
    elif x == "as" or x == "sa":
        ncol -=1
        nrow += 1
    elif x == "wa" or x == "aw":
        nrow -=1
        ncol -=1
    
    if canmove(nrow, ncol,array):
        return nrow,ncol
    return Player_row,Player_col