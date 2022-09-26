# Name: Regan Yang
# Email: reyang@ucsd.edu
#
# Minesweeper 9x9
# Rules: 
# 1) when a square is selected, it will check its surroundings top, bottom
# left, right, and diagonals for bombs and indicate number of bombs. 
# 2) In case where there's no bombs, will check its neighbor squares for bombs, 
# repeats if there's no bombs. Ends when all squares have at least 1 bomb as a neighbor
# 3) The first selected square will never contain a bomb
# 4) Game is lost if selected square is a bomb
# 5) All ' ' will represent empty squares, numerical squares and 's' will represent selected squares.
# 's' squares means there are no neighboring bombs.
# Squares with no neighboring bombs in rule 2) will also be considered selected squares.
# 'x' will represent bombs, this will only show when the game is lost
# The user may use "flags" to represent squares where the user thinks is a bomb. All flags
# will be represented as "F" on the board. Flags are optional!
# 6) TO INPUT SQUARES, MUST BE NUMERICAL FORMAT. e.g
# Select square at [6][6], input must be 66 
# FOR SQUARES on the 0th row, single digit or coordinate style e.g 06, 05
# 7) To win, all available squares have to be bombs

from functions import *

rows, cols = (9, 9)
board = [[' ' for i in range(cols)] for j in range(rows)]
bombBoard = [[' ' for i in range(cols)] for j in range(rows)]
printBoard(board)
selectPos = promptInput(board)
bombList = []
generate(bombList, selectPos, bombBoard)
#for win con, we make a list of avail squares, when the list = bomb list, you win
availList = []
#Since it's 9x9 starting from row, col = 0, we remove out of bounds squares
removeSq = {9, 19, 29, 39, 49, 59, 69, 79}
availList.extend(range(0, maxNumSize))
for square in removeSq:
    availList.remove(square)

availList.sort()
status = True
printBoard(bombBoard)
branchOut(board, selectPos, bombBoard, availList)
printBoard(board)
while(True):
    # num form
    print("availList: ", availList)
    print("bombList: ", bombList)
    pos = promptInput(board)
    if(availList.count(pos) > 0):
        availList.remove(pos)
    #check if we selected a bomb
    posList = numToList(pos)
    #checks if selection is on a bomb
    if(bombBoard[posList[0]][posList[1]] == 'x'):
        status = False
        break
    branchOut(board, pos, bombBoard, availList)
    if(availList == bombList):
        status = True
        break
    printBoard(board)

gameOver(board, bombList, status)

