class Command_Line:
    """Command Line Interface that user interacts with."""

    @staticmethod
    def start_new_game():
        """Displays the welcome messages."""
        print("\nWelcome to Tic Tac Toe!")
        print("You may enter 'q' at any time to quit.\n")
        
    @staticmethod
    def show_board(board, final_board):
        """Displays a given board"""
        if final_board:
            print("The final board looks like this!")
        else:
            print("\nThe current board looks like this.")

        print(board[0][0] + ' ' + board[0][1] + ' ' + board[0][2])
        print(board[1][0] + ' ' + board[1][1] + ' ' + board[1][2])
        print(board[2][0] + ' ' + board[2][1] + ' ' + board[2][2] + '\n')

    @staticmethod
    def valid_move_input(move):
        """Helper function that checks and returns if a given move is valid"""
        if move == "q":
            return True

        if len(move) != 3:
            return False
        if not move[0].isdigit() or int(move[0]) not in range(1, 4):
            return False
        if move[1] != ",":
            return False
        if not move[2].isdigit() or int(move[2]) not in range(1, 4):
            return False

        return True

    def get_move(self, player):
        """Collects a move for a given player and returns the move (row, col) or q if the user quits."""
        if player == 1:
            token = 'X'
        else:
            token = 'O'
        move = input("\nPlayer {} ({}), where would you like to go?\n".format(player, token))

        while not self.valid_move_input(move):
            print("\nThat is not a valid move!\n" +
                  "Rows and columns should range from 1 - 3 and be in the format row,column. eg. 2,1")
            
            move = input("Player {} ({}), where would you like to go?\n".format(player, token))
        
        if move == "q":
            return move

        return int(move[0]), int(move[2])

    @staticmethod
    def move_already_taken():
        """Gives feedback that a move is already taken."""
        print("\nThat move is already taken! Please choose another.")

    @staticmethod
    def end_game(winner):
        """Displays the end game message."""
        if winner != None:
            print("\nPlayer {} wins!".format(winner))
        else:
            print("\nThis game was a draw!")

    @staticmethod
    def play_again():
        """Returns if the players would like to play again."""
        valid_input = ["y", "n", "yes", "no", "q"]
        answer = input("\nWould you like to play again? (y/n)\n").lower()

        while answer not in valid_input:
            print("\nSorry, I don't know what you mean...")
            answer = input("Would you like to play again? (y/n)\n")

        if answer == "y" or answer == "yes":
            return True
        else:
            return False

    @staticmethod
    def quit():
        """Displays the quit message."""
        print("\nThanks for playing!")
