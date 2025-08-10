
"""
Requirements (from your understanding of the problem)

-> a standard 3x3 board (grid)

-> Two players taking turns and marking "X" or "O" in their respective move if VALID.

-> The game continues until:

- either of the player get their marks in a line (horizontal, vertical, diagonal (both) ).

- The game ends in draw (no more empty spaces left to mark)


** Important ** -  ask for any other core requirements that he wants me tp focus on such as board size, 2- player or more. The interviewer may tell you to focus on core things like:-

-> move validation to ensure no invalid moves

-> detection of Win or Draw scenarios

"""

"""
-> Start Identifying key components/entitites/classes (lookup in the requirements for identifying)
"""
 


from enum import Enum
from abc import ABC, abstractmethod


class Symbol(Enum):
    X = 0
    O = 1
    EMPTY = 2

class GamesState(Enum):
    Win = 0
    DRAW = 1
    IN_PRPGRESS = 2


# class Player:
#     pass


# class Board:
#     pass



"""
Talking about Design Patterns here:-
-> Strategy pattern could be implemented for different players having their own makeMove()
-> Factory pattern could be incorportated for creation of different players.


In Future:-
-> State pattern can manage player status changes, either switching to the next player’s turn or updating the current player to winner."
-> Observer pattern could be included to notify players about their turn, log details, game status changed etc.
"""


#Strategy Pattern Simple Implementation
class Position:
    def __init__(self,row,col):
        self.row=row
        self.col=col



@abstractmethod
class PlayerStrategy(ABC):
    def makeMove(board: Board):
        pass



class HumanPlayerStrategy(PlayerStrategy):
    def makeMove(board: Board):
        while True:
            row= int(input())
            col = int(input())

            position = Position(row,col)

            if board.isValidMove(position):
                return position
            else:
                print("Invalid Move! Please Try Again!")
            


#in future implementation
class AIPlayerStrategy(PlayerStrategy):
    def makeMove(board: Board):
        pass










#Factory Pattern Simple Implementation
class Player:
    def __init__(self,name,symbol,strategy):
        self.name=name
        self.symbol = symbol
        self.strategy = strategy

    def makeMove(self,board):
        return self.strategy.makeMove(board)
    
    def getSymbol(self):
        return self.symbol
    

class HumanPlayer(Player):
    pass


class AiPlayer(Player):
    pass


class PlayerFactory():
    @staticmethod
    def create_player(name,symbol,typeOfPlayer):
        if typeOfPlayer == "human":
            return HumanPlayer(name, symbol, HumanPlayerStrategy())
        
        elif typeOfPlayer == "ai":
            return AiPlayer(name, symbol, AIPlayerStrategy())
        
        else:
            raise ValueError("Unknown player type")

#code calls 
# p1 = PlayerFactory.create_player("Alice", Symbol.X, "human")  # returns HumanPlayer(...)
# p2 = PlayerFactory.create_player("Bot", Symbol.O, "ai")       # returns AiPlayer(...)




#Implementing main board class
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
        if position.row == position.col:
            leftDiagCheck=True
            for i in range(self.rows):
                if self.grid[i][i] != symbol:
                    leftDiagCheck = False
                    break

        #check right diagonal
        if position.row == self.cols -  position.col -1:
            rightDiagCheck=True
            for i in range(0,self.rows):
                if self.grid[i][self.cols - i -1]!=symbol:
                    rightDiagCheck=False
                    break
        
        return rowCheck or colCheck or leftDiagCheck or rightDiagCheck


    def isFull(self):
        return  self.empty_count == 0

        

        

class BoardGames(ABC):

    @abstractmethod
    def play():
        pass


class TicTacToe(BoardGames):
    def __init__(self):
        self.board = Board(3,3)
        self.playerA = PlayerFactory.create_player("Aryan",Symbol.X,"human")
        self.playerB= PlayerFactory.create_player("Vedangi",Symbol.O,"human")
        self.currPlayer = self.playerA
        self.currGameState = GamesState.IN_PRPGRESS


    def play(self):

        while self.currGameState == GamesState.IN_PRPGRESS:
            pos = self.currPlayer.makeMove(self.board)
            self.board.applyMove(pos, self.currPlayer.getSymbol())
            if self.board.checkWinner(self.currPlayer.getSymbol(), pos):
                self.currGameState = GamesState.Win
            elif self.board.isFull():
                self.currGameState = GamesState.DRAW
            else:
                self.swapPlayers()
            
            
            self.board.printBoard()
                
      
        
        self.announceResult()
    
    
    def announceResult(self):
        if self.currGameState == GamesState.DRAW:
            print("Match Drawn! Well Played.")
        else:
            if self.currPlayer == self.playerA:
                print(f"${self.playerA.name} Won! Well Played ${self.playerB.name}")
            else:
                print(f"${self.playerB.name} Won! Well Played ${self.playerA.name}")
    
    def swapPlayers(self):
        if self.currPlayer == self.playerA:
            self.currPlayer = self.playerB
        else:
            self.currPlayer = self.playerA




if __name__ == "__main__":
    game = TicTacToe()
    game.play()
