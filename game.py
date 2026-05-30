# main game file, handles backend
import random

# 0 = blocked, 1 = open, S = start, E = end

puzzles = [
    {
        "rows": 4,
        "cols": 4,
        "S": (0, 0),
        "E": (3, 3),
        "X": [(1, 2)]
    },
    {
        "rows": 5,
        "cols": 5,
        "S": (0, 0),
        "E": (4, 4),
        "X": [(0, 1), (0, 4), (1, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 2)]

    },
    {
        "rows": 5,
        "cols": 5,
        "S": (0, 0),
        "E": (4, 4),
        "X": [(1, 2), (2, 2), (2, 3)]
    },

    {
        "rows": 5,
        "cols": 5,
        "S": (0, 4),
        "E": (4, 0),
        "X": [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (2, 4), (3, 1), (3, 3), (4, 2), (4, 4)]
    },

    {
        "rows": 5,
        "cols": 4,
        "S": (0, 3),
        "E": (2, 2),
        "X": [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1)]
    },

    {
        "rows": 4,
        "cols": 4,
        "S": (3, 2),
        "E": (3, 0),
        "X": [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1)]
    },

    {
        "rows": 5,
        "cols": 5,
        "S": (3, 3),
        "E": (2, 2),
        "X": [(1, 1), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
    },

    {
        "rows": 4,
        "cols": 5,
        "S": (0, 4),
        "E": (2, 2),
        "X": [(1, 1), (1, 2), (1, 3), (2, 3)]
    },

    {
        "rows": 4,
        "cols": 4,
        "S": (0, 3),
        "E": (3, 3),
        "X": [(1, 1), (1, 3), (2, 2), (3, 1)]
    },

    {
        "rows": 4,
        "cols": 4,
        "S": (0, 0),
        "E": (3, 3),
        "X": [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1)]
    },

    {
        "rows": 4,
        "cols": 4,
        "S": (3, 3),
        "E": (0, 0),
        "X": [(0, 3)]
    }
]

chosen = random.choice(puzzles)

array = []

#setting zone - dangerous
rows = chosen["rows"]
cols = chosen["cols"]

#positions
S_row = chosen["S"][0]
S_col = chosen["S"][1]

E_row = chosen["E"][0]
E_col = chosen["E"][1]

X_pos = chosen["X"]

Player_row = S_row
Player_col = S_col

game = True

# grid zone
def grid():
    global array, rows, cols
    for _ in range(rows):
        array.append([1] * cols)

def set_X():
    global X_pos

    for x in X_pos:
        row = x[0]
        col = x[1]
        array[row][col] = 0 #0th index!

def set_Start():
    global S_row,S_col
    array[S_row][S_col] = "S"

def set_End():
    global E_row,E_col
    array[E_row][E_col] = "E"

def Setup():
    grid()
    set_Start()
    set_End()
    set_X()

def output():
    rdisplay = [row[:] for row in array]

    rdisplay[Player_row][Player_col] = "P"

    for row in rdisplay:
        print(row)
    
    print()

#player zone

def canmove(row,col):
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False

    elif array[row][col] == 0:
        return False
    
    else:
        return True

# testing zone...
Setup()
output()

#gamezone!

while game == True:
    x = str(input("Move with W/A/S/D/WD/SD/AS/WA"))

    nrow = Player_row
    ncol = Player_col

    if x == "W" or x == "w":
        nrow -=1
    elif x == "S" or x == "s":
        nrow += 1
    elif x == "A" or x == "a":
        ncol -=1
    elif x == "D" or x == "d":
        ncol += 1
    elif x == "WD" or x == "wd":
        nrow -=1
        ncol +=1
    elif x == "SD" or x == "sd":
        nrow += 1
        ncol += 1
    elif x == "AS" or x == "as":
        ncol -=1
        nrow += 1
    elif x == "WA" or x == "wa":
        nrow -=1
        ncol -=1
    
    if canmove(nrow, ncol) == True:
        Player_row = nrow
        Player_col = ncol
    else:
        print("nah")
    
    output()

    if Player_row == E_row and Player_col == E_col:
        print("yay")
        game = False
    