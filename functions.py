# Name: Regan Yang
# EmaiL: reyang@ucsd.edu
#
# The purpose of this file is to store all the functions used  by minesweeper.py.
# This helps the code look cleaner.
 
import queue
from random import *

numBombs = 10
maxNumSize = 89

# convert from list format to Num
# e.g [1,1] = 11, [2,3] = 23, [0,1] = 1
# @param: 
# - listNum: number in list form
# @return: number in numerical form
def listToNum(listNum):
    if(isinstance(listNum, int)):
        return listNum
    if(not isinstance(listNum, list) or len(listNum) > 2):
        return print("Argument not a list or invalid size")
    num1 = listNum[0]
    num2= None
    if(len(listNum) == 2):
        num2 = listNum[1]
    match num1:
        case 0:
            if(len(listNum) == 2):
                return listNum[1]
            return listNum[0]
        case _:  
            if(len(listNum) == 2):
                return listNum[1] + listNum[0]*10
            return listNum[0]

# convert from numbers to list format
# e.g 10 = [1, 0], 1 = [0,1]
# @param: 
# - num: the number that is to be converted to list form
# @return: list form of num
def numToList(num):
    if(isinstance(num, list)):
        return num
    firstDig = int(num % 10)
    secondDig = int(num / 10)
    numList = [secondDig, firstDig]
    return numList

# prints the current state of the board
# @param
# - list: the board we want to print
def printBoard(list):
    print(" # 0 1 2 3 4 5 6 7 8 #")
    print("  -------------------")
    for num, row in enumerate(list):
        print(num," |",end="", sep="")
        for elements in row:
            print(elements,"|", end="", sep="")
        print("")

# mark flags
# @param:
# - board: the board to place flags on
# - pos: the square to put the flag in
def markFlags(board, pos):
    coord = numToList(pos)
    board[coord[0]][coord[1]] = 'F'
    printBoard(board)

# prompt select square or place flag, only numerical selections 
# e.g input 65 = [6][5], 6 = [0][6]
# Only values that are within the coordinate system will be accepted.
# @param: 
# - board: board to place select square in
# @return: value of valid selected square
def promptInput(board):
    status = True
    val = 0
    while status:
        try:
            if(status == False):
                break
            choice = int(input("Input 0 to select Square or Input 1 to place flag: "))
            print("if selection was a mistake, type in anything as long as it's not a number between 0 and 88")
            if(choice == 0):
                val = int(input("Select Square: "))
                if(val <= 88 and val >= 0):
                    valList = numToList(val)
                    if(board[valList[0]][valList[1]] != ' 'and 
                        board[valList[0]][valList[1]] != 'F'):
                        print(board[valList[0]][valList[1]])
                        print("Invalid square! Try again.")
                        continue
                    status = False
                    break
                print("Value not between 0 and 88, try again!")
            elif(choice == 1):
                flag = int(input("Flag position: "))
                if(flag <= 88 and flag >= 0):
                    valList = numToList(flag)
                    if(board[valList[0]][valList[1]] != ' 'and 
                        board[valList[0]][valList[1]] != 'F'):
                        print("Invalid square! Try again.")
                        continue
                    markFlags(board, flag)
                    continue
                print("Value not between 0 and 88, try again!")
            else:
                print("Didn't select a value of 0 or 1")
        except ValueError:
            print("Not an integer, try again!")
        except IndexError:
            print("Please choose within the coordinate system")
    return val

# finds neighboring squares and makes a list of them
# @param 
# - pos: coordinate in num form
# @return a list of spots bombs shouldn't be in
def posBombsRemove(pos):
    coord = numToList(pos)
    row = coord[0]
    col = coord[1]
    bombToRemove = []
    if(col != 0):
        bombToRemove.append(listToNum([row, col-1]))
    #Right
    if(col != 8):
        bombToRemove.append(listToNum([row, col+1]))
    #Top
    if(row != 0):
        bombToRemove.append(listToNum([row-1, col]))
    #Bot
    if(row != 8):
        bombToRemove.append(listToNum([row+1, col]))
    #Top Left
    if(col != 0 and row != 0):
        bombToRemove.append(listToNum([row-1, col-1]))
    #Top Right
    if(col != 8 and row != 0):
        bombToRemove.append(listToNum([row-1, col+1]))
    #Bot Left
    if(col != 0 and row != 8):
        bombToRemove.append(listToNum([row+1, col-1]))
    #Bot Right
    if(col != 8 and row != 8):
       bombToRemove.append(listToNum([row+1, col+1]))
    return bombToRemove

# create list of bombs and update their positions on bBoard
# @param: 
# - bombs: list of bombs
# - pos: position of initial selected square
# - bBoard: board for bomb positions
def generate(bombs, pos, bBoard):
    numList = []
    bombsRemoveSet = {9, 19, 29, 39, 49, 59, 69, 79}
    numList.extend(range(0, maxNumSize))
    numList.pop(pos)
    bombsRemoveSet.update(posBombsRemove(pos))
    for bomb in bombsRemoveSet:
        numList.remove(bomb)
    bombList = sample(numList,numBombs)
    for i in bombList:
        bombs.append(i)
        bCoord = numToList(i)
        bBoard[bCoord[0]][bCoord[1]] = 'x'
    bombs.sort()   

# checks neighbors for bombs!
# places selected squares in board
# @param:
# - bBoard: a 2D list with position of bombs 
# - board: the board the user sees
# - pos: the position selected
# @return: returns the # of neigh bombs and their locations in list form
def bombCheck(bBoard, pos, board):
    # addToQueue's first element will be the num of bombs
    # then the rest will be coordinates for squares that don't contain bombs
    addToQueue = [0]
    numBombs = 0
    position = numToList(pos)
    row = position[0]
    col = position[1]
    #left
    if(col != 0):
        if(bBoard[row][col-1] != 'x'):
            if(board[row][col-1] != 's'):
                addToQueue.append([row, col-1])
        else:
            numBombs+=1
    #Right
    if(col != 8):
        if(bBoard[row][col+1] != 'x'):
            if(board[row][col+1] != 's'):
                addToQueue.append([row, col+1])
        else:
            numBombs+=1
    #Top
    if(row != 0):
        if(bBoard[row-1][col] != 'x'):
            if(board[row-1][col] != 's'):
                addToQueue.append([row-1, col])
        else:
            numBombs+=1
    #Bot
    if(row != 8):
        if(bBoard[row+1][col] != 'x'):
            if(board[row+1][col] != 's'):
                addToQueue.append([row+1, col])
        else:
            numBombs+=1
    #Top Left
    if(col != 0 and row != 0):
        if(bBoard[row-1][col-1] != 'x'):
            if(board[row-1][col-1] != 's'):
                addToQueue.append([row-1, col-1])
        else:
            numBombs+=1
    #Top Right
    if(col != 8 and row != 0):
        if(bBoard[row-1][col+1] != 'x'):
            if(board[row-1][col+1] != 's'):
                addToQueue.append([row-1, col+1])
        else:
            numBombs+=1
    #Bot Left
    if(col != 0 and row != 8):
        if(bBoard[row+1][col-1] != 'x'):
            if(board[row+1][col-1] != 's'):
                addToQueue.append([row+1, col-1])
        else:
            numBombs+=1
    #Bot Right
    if(col != 8 and row != 8):
        if(bBoard[row+1][col+1] != 'x'):
            if(board[row+1][col+1] != 's'):
                addToQueue.append([row+1, col+1])
        else:
            numBombs+=1
    addToQueue[0] = numBombs
    return addToQueue

# Queue will be in numerical format e.g 11, 22, 13
# Selected square will be put into Queue and popped from Queue has no neighboring bombs, 
# update board for pos as 's' and adds its neighbors to queue. Repeats until all current neighbors for
# select squares have a neighboring bomb. Will update list of available squares.
# @param:
# - board: board to update from
# - pos: position of selected square in numerical form
# - bBoard: board with only bomb positions
# - availList: list of available squares
def branchOut(board, pos, bBoard, availList): 
    q = queue.Queue(0)
    firstPos = numToList(pos)
    row, col = firstPos[0], firstPos[1]
    board[row][col] = 's'
    q.put(firstPos)
    while(not q.empty()):
        coord = q.get()
        availSq = bombCheck(bBoard, coord, board)
        coord = numToList(coord)
        #availSq[0] is num of bombs, rest is coord of available squares
        if(availSq[0] > 0):
            board[coord[0]][coord[1]] = f'{availSq[0]}'
            if(availList.count(listToNum([coord[0], coord[1]])) > 0):
                availList.remove(listToNum([coord[0], coord[1]]))
        else:
            if(availSq[0] == 0):
                board[coord[0]][coord[1]] = 's'
                if(availList.count(listToNum([coord[0], coord[1]])) > 0):
                    availList.remove(listToNum([coord[0], coord[1]]))
            if(len(availSq) > 1):
                #specific loop through availSq ( not include first ele)
                #put availSq into Q
                for i in range(1, len(availSq)-1):
                    list = listToNum(availSq[i])
                    q.put(list)

# plant bombs for game over screen
# @param:
# - board: 2d list of the board
# - bombs: list of bombs
# - status: true for win, false for lose
def gameOver(board, bombs, status):
    for element in bombs:
        coord = numToList(element)
        board[coord[0]][coord[1]] = 'x'
    printBoard(board)
    if(status):
        print("YOU WIN!!")
    else:
        print("GAME OVER!")