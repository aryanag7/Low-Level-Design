from tic_tac_toe import TicTacToe

if __name__ == "__main__":
    game = TicTacToe()
    game.play()




"""
We started with a basic TicTacToe idea:
- A 3x3 grid
- Two players taking turns marking X or O
- Win/Draw detection

Extensions we implemented:
- BoardGames interface for supporting multiple types of board games in future
- Strategy pattern for different player types (Human vs AI)
- Factory pattern for easy player creation without changing core game logic
- AIPlayerStrategy with a simple 'take center first' + random move logic
- Input validation for Human moves
- Separation of classes (Board, Player, Position, Strategy) for cleaner design

Possible future extensions:
- More advanced AI (minimax, blocking opponent's winning move)
- Custom board sizes (NxN)
- Multiple players instead of only 2
- Save/Load game state for resuming later
- GUI or Web-based interface
- Observer pattern to notify players or spectators when game state changes
- State pattern to manage different stages of the game (Setup, Playing, Finished)
"""


# Observer Pattern Note:
# We can use Observer here so that external components (like a logger, UI, or stats tracker)
# can be "subscribed" to the game and get notified whenever important events happen 
# (e.g., a move made, game won, or drawn) without changing the game logic itself.
# This makes the design more modular, easy to extend, and follow the open/closed principle.
# A new Subject class can inherit from TicTacToe, add observer management methods 
# (attach, detach, notify), and still use all TicTacToe's game logic.
