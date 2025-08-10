from abc import ABC, abstractmethod
from board import Board
from position import Position

@abstractmethod
class PlayerStrategy(ABC):
    def makeMove(self, board: Board):
        pass


class HumanPlayerStrategy(PlayerStrategy):
    def makeMove(self, board: Board):
        while True:
            row, col = map(int, input("Enter row and column: ").split())
            
            position = Position(row,col)

            if board.isValidMove(position):
                return position
            else:
                print("Invalid Move! Please Try Again!")
            


#in future implementation
class AIPlayerStrategy(PlayerStrategy):
    def makeMove(self,board: Board):
        pass

