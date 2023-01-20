board = [
        [3, 0, 0, 8, 0, 1, 0, 0, 2],
        [2, 0, 1, 0, 3, 0, 6, 0, 4],
        [0, 0, 0, 2, 0, 4, 0, 0, 0],
        [8, 0, 9, 0, 0, 0, 1, 0, 6],
        [0, 6, 0, 0, 0, 0, 0, 5, 0],
        [7, 0, 2, 0, 0, 0, 4, 0, 9],
        [0, 0, 0, 5, 0, 9, 0, 0, 0],
        [9, 0, 4, 0, 8, 0, 7, 0, 5],
        [6, 0, 0, 1, 0, 7, 0, 0, 3]
    ]

def solve(bo):
    #if find the empty
    #print(bo)
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    #loop through 1-9 and try to put in solution
    for i in range(1,10):
        #plug in the value in board if its valid
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            
            #try to finish solution by recursively calling solve
            if solve(bo):
                return True

            bo[row][col] = 0
            #above is to backtrack and reset the last value to 0 - solve()!=true

    return False #if no solution is found that pos


def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        #check each element in row if added number in pos matches
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(bo)):
        #check each element in col if added number in pos matches
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    #get box position by integer division
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x* 3 +3):
            if bo[i][j] == num and (i,j) != pos:
                return False
                
    return True


def print_board(bo) :
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")  #print horizontal line every third row

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")  #print line after 3rd col number and end part prevents newline

            #if at end number of line, do \n to go to next line
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") 


def find_empty(bo):
    #loop to traverse in 2d array
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j) #row, col

    return None  #no blank squares


print_board(board)


solve(board)
print(">>>>>>>>>>>>>>>>>>>>>>")
print_board(board)
