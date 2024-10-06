import numpy as np
import pandas as pd
import random

def createNewBoard(puzzle):
        puzzle = list(str(puzzle))
        return np.array(puzzle).reshape(9, 9)
    
def printBoard(board):
    printLine()
    print()
    for i in range(9):
        print("|", end = " ")
        for j in range(9):
            print(board[i][j], end = " | ")
        print()
        if i % 3 == 2:
            printLine()
            print()

def printLine():
    for x in range(19):
        if x % 6 == 0:
            print("|", end = " ")
        else:
            print("-", end = " ")
def removeIncorrect(board, solution):
    for i in range(9):
        for j in range(9):
            if board[i][j] != solution[i][j]:
                board[i][j] = 0
    return board

def main():
    df = pd.read_csv('sudoku.csv')
    puzzle_number = random.randint(0, 9000000)
    board = createNewBoard(df.iloc[puzzle_number, 0])
    solution = createNewBoard(df.iloc[puzzle_number, 1])
    while True:
        printBoard(board)
        print("Enter the row and column of the cell you want to fill in (0-indexed) or -1 to quit")
        row = int(input("Row: "))
        if row > 9 or row < 1:
            print("Invalid row")
            break
        col = int(input("Column: "))
        if col > 9 or col < 1:
            print("Invalid column")
            break
        if board[row - 1][col - 1] != 0:
            print(board[row - 1][col - 1])
            print("Cell already filled")
            break
        print("Enter the number you want to fill in the cell")
        num = int(input("Number: "))
        if num > 9 or num < 1:
            print("Invalid number")
            break
        board[row - 1][col - 1] = num
        if (board == solution).all():
            print("You have solved the puzzle!")
            break
        else:
            if np.all(board):
                print("You have filled all the cells but the solution is incorrect")
                print("Removing incorrect cells")
                board = removeIncorrect(board, solution)
                break


    


if __name__ == '__main__':
    main()