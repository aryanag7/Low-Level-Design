from board import Board
from player import PlayerFactory
from board_games import BoardGames
from game_state import GamesState
from symbol import Symbol


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
                print(f"{self.playerA.name} Won! Well Played {self.playerB.name}")
            else:
                print(f"{self.playerB.name} Won! Well Played {self.playerA.name}")
    
    def swapPlayers(self):
        if self.currPlayer == self.playerA:
            self.currPlayer = self.playerB
        else:
            self.currPlayer = self.playerA


