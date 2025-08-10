from abc import ABC, abstractmethod
from board import Board
from position import Position
from symbol import Symbol
import random

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
    def take_center_first(self, board:Board):
        center_pos = Position(board.rows//2 , board.cols//2)
        if board.isValidMove(center_pos):
            return center_pos
        return None

    def makeMove(self, board: Board):
        center_move = self.take_center_first(board)
        if center_move:
            return center_move

        empty_positions = []
        for i in range(0,board.rows):
            for j in range(0, board.cols):
                if board.grid[i][j] == Symbol.EMPTY:
                    empty_positions.append(Position(i,j))
        
        return random.choice(empty_positions)



        
        

