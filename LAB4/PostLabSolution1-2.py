''' This is the main logic for a Tic-tac-toe game using OOP.
It is not optimized for a quality game; it simply
generates random moves and checks the results.
'''

import random
import oxo_data

class Game:
    def __init__(self):
        self.board = list(" " * 9)

    @classmethod
    def restore(cls):
        ''' Restores a saved game or creates a new one if failed '''
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                g = cls()
                g.board = game
                return g
            else:
                return cls()
        except IOError:
            return cls()

    def save(self):
        ''' Save current game state '''
        oxo_data.saveGame(self.board)

    def _generateMove(self):
        ''' Generate a random valid cell, or -1 if full '''
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        return random.choice(options) if options else -1

    def _isWinningMove(self):
        ''' Check if the current board has a winning line '''
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))
        for a, b, c in wins:
            line = self.board[a] + self.board[b] + self.board[c]
            if line == 'XXX' or line == 'OOO':
                return True
        return False

    def userMove(self, cell):
        ''' Apply user move and check for win '''
        if self.board[cell] != ' ':
            raise ValueError("Invalid cell")
        self.board[cell] = 'X'
        return 'X' if self._isWinningMove() else ""

    def computerMove(self):
        ''' Let computer play a random valid move '''
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        return 'O' if self._isWinningMove() else ""

    def isDraw(self):
        return " " not in self.board

    def display(self):
        ''' Optional: Pretty print board '''
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("--+---+--")


def test():
    result = ""
    game = Game()
    while not result:
        game.display()
        try:
            result = game.userMove(game._generateMove())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = game.computerMove()
        if result == 'D':
            print("It's a draw")
        elif result in ('X', 'O'):
            print("Winner is:", result)
            game.display()
            break


if __name__ == "__main__":
    test()
