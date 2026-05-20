# main game file, handles backend

array = []

#setting zone - dangerous
rows = 2
cols = 3

def grid():
    global array, rows, cols
    for _ in range(rows):
        array.append([1] * cols)
    return array

def set_X(row,col):
    array[row][col] = 0 #0th index!

def set_Start(row,col):
    array[row][col] = "S"

def set_End(row,col):
    array[row][col] = "E"

def output():
    for x in range(rows):
        print(array[x])



# testing zone...
grid()
set_Start(0,0)
set_End(1,2)
set_X(1,1)
output()
