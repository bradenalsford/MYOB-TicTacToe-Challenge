class Game:
    """A game of Tic Tac Toe."""

    def __init__(self):
        self.current_player = 1
        self.turn_count = 0
        self.complete = False
        self.winner = None
        self.board = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]
        
    def change_player(self):
        """Swaps the current player."""
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def increment_turn(self):
        """Increases the turn count by one."""
        self.turn_count += 1

    def move_available(self, move):
        """Returns a boolean representing if a given move, (row, col), is available."""
        row, col = move
        return self.board[row - 1][col - 1] == '.'
        
    def update_board(self, move):
        """Updates the game board with a given move, (row, col), for the current player."""
        row, col = move
        if self.current_player == 1:
            self.board[row - 1][col - 1] = 'X'
        else:
            self.board[row - 1][col - 1] = 'O'
        
    def update_game(self, move):
        """Checks if the game is complete and assigns a winner if applicable."""
        row = move[0] - 1
        col = move[1] - 1
        
        # Check vertical
        if self.board[0][col] == self.board[1][col] == self.board[2][col]:
            self.complete = True
            self.winner = self.current_player

        # Check horizontal
        elif self.board[row][0] == self.board[row][1] == self.board[row][2]:
            self.complete = True
            self.winner = self.current_player

        # Check first diagonal
        elif row == col and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.complete = True
            self.winner = self.current_player

        # Check second diagonal
        elif row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.complete = True
            self.winner = self.current_player

        # Check if there is no winner.
        elif self.turn_count == 9:
            self.complete = True

    def process_turn(self, move):
        """Takes a move, (row, col), and completes the required actions associated with a valid turn"""
        self.update_board(move)
        self.increment_turn()
        self.update_game(move)

        if not self.complete:
            self.change_player()
