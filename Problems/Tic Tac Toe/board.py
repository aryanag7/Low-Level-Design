from symbol import Symbol
from position import Position

class Board:
    def __init__(self,rows,columns):
        self.rows = rows
        self.cols = columns
        self.empty_count = self.rows * self.cols


        self.grid = [[ Symbol.EMPTY for j in range(self.cols)] for i in range(self.rows)]
    
    def isValidMove(self,position : Position):
        return position.row >= 0 and position.row < self.rows and position.col >=0 and  position.col <  self.cols and self.grid[position.row][position.col] == Symbol.EMPTY


    def applyMove(self,position : Position, symbol: Symbol):
        self.grid[position.row][position.col] = symbol
        self.empty_count-=1

    def printBoard(self):
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                print(self.grid[i][j].name, end=" ")
            print()
        
    def checkWinner(self, symbol: Symbol, position: Position):
        #check curr row
        rowCheck=True
        for i in range(0,self.cols):
            if self.grid[position.row][i] != symbol:
                rowCheck=False
                break


        colCheck=True
        #check curr column
        for i in range(0,self.rows):
            if self.grid[i][position.col] != symbol:
                colCheck= False
                break


        #check left diagonal
        leftDiagCheck=False
        if position.row == position.col:
            temp=True
            for i in range(self.rows):
                if self.grid[i][i] != symbol:
                    temp = False
                    break

            leftDiagCheck = temp


        #check right diagonal
        rightDiagCheck = False
        if position.row == self.cols -  position.col -1:
            temp=True
            for i in range(0,self.rows):
                if self.grid[i][self.cols - i -1]!=symbol:
                    temp=False
                    break
            rightDiagCheck = temp
        
        return rowCheck or colCheck or leftDiagCheck or rightDiagCheck


    def isFull(self):
        return  self.empty_count == 0
