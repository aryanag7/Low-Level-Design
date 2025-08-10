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
