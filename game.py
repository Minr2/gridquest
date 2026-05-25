# main game file, handles backend

array = []

#setting zone - dangerous
rows = 2
cols = 3
game = True

#positions
S_row = 0
S_col = 0

E_row = 1
E_col = 2

X_pos = [0,1]

Player_row = S_row
Player_col = S_col

# grid zone
def grid():
    global array, rows, cols
    for _ in range(rows):
        array.append([1] * cols)

def set_X():
    global X_pos
    array[X_pos[0]][X_pos[1]] = 0 #0th index!

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

    for x in range(len(rdisplay)):
        print(rdisplay[x])

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
    x = str(input("Move with W/A/S/D"))

    nrow = Player_row
    ncol = Player_col

    if x == "W":
        nrow -=1
    elif x == "S":
        nrow += 1
    elif x == "A":
        ncol -=1
    elif x == "D":
        ncol += 1
    
    if canmove(nrow, ncol) == True:
        Player_row = nrow
        Player_col = ncol
    else:
        print("nah")
    
    output()

    if Player_row == E_row and Player_col == E_col:
        print("yay")
        game = False
    
    