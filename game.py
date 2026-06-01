# main game file, handles backend
import random

# 0 or X = blocked, 1 = open, S = start, E = end, T = star
from puzzles import advanced_puzzles, beginner_puzzles

difficulty = input("Choose difficulty: beginner/advanced").lower() #lower removes UPPERCASE

if difficulty == "advanced":
    chosen = random.choice(advanced_puzzles)
    advmode = True
else:
    chosen = random.choice(beginner_puzzles)
    advmode= False

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
T_pos = chosen["T"]

Player_row = S_row
Player_col = S_col

#stars
collected_stars = set()
totalstars = set(T_pos)
visited = set()
visited.add((Player_row,Player_col))

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

def set_T():
    global T_pos

    for x in T_pos:
        row = x[0]
        col = x[1]
        array[row][col] = "T"

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
    set_T()

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

    if array[row][col] == 0:
        return False
    
    if advmode == True:
        if (row,col) in visited:
            print("u already visited")
            return False
        
        if array[row][col] == "E" and collected_stars != totalstars:
            print("collect all stars first")
            return False

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

        if advmode == True:
            visited.add((Player_row, Player_col))

            if array[Player_row][Player_col] == "T":
                collected_stars.add((Player_row, Player_col))
                print("collected star")
    else:
        print("nah")
    
    output()

    if Player_row == E_row and Player_col == E_col:
        if advmode == True:
            if collected_stars == totalstars:
                print("yay")
                game = False
        else:
            print("yay")
            game = False
    