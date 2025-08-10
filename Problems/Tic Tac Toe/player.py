from player_strategy import HumanPlayerStrategy,AIPlayerStrategy

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
        