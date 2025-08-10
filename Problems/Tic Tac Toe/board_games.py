from abc import ABC, abstractmethod

class BoardGames(ABC):
    @abstractmethod
    def play():
        pass



"""
The BoardGames interface defines a common contract for all board games.
By having an abstract play() method, we ensure that any game (TicTacToe, Chess, Checkers, etc.)
can be started in a consistent way.

Benefits:
- Extensibility: Easily add new games by creating new classes that implement this interface.
- Polymorphism: Code can work with any 'BoardGames' type without knowing the exact game.
- Standardization: All board games must follow the same structure for starting/playing.
- Save/Load Support: In the future, we can extend this interface with methods like save_game()
  and load_game(), allowing any game to implement its own persistence logic.

Without this interface, our TicTacToe would work, but adding new games or features like save/load
would require rewriting logic instead of reusing the same structure.
"""




