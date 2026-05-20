# main game file, handles backend

array = []

#setting zone - dangerous
rows = 2
cols = 3

# grid zone
def grid():
    global array, rows, cols
    for _ in range(rows):
        array.append([1] * cols)
    return array

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
    set_Start()
    set_End()
    set_X()

def output():
    for x in range(rows):
        print(array[x])

#player zone

S_row = 0
S_col = 0
E_row = 1
E_col = 2
X_pos = [0,1]

def init_Player():
    global PlayerX,PlayerY
    PlayerX = S_row
    PlayerY = S_col


# testing zone...
grid()
set_Start()
set_End()
set_X()
output()
