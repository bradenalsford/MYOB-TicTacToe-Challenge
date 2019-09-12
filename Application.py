import sys
from Command_Line import Command_Line
from Game import Game


class Application:
    """Controls the connection between gameflow and the command line interface."""
    
    def leave_game(self, client):
        """Helper function that takes the client and closes the game"""
        client.quit()
        sys.exit()


    def run(self):
        """Runs games of Tic Tac Toe"""
        client = Command_Line()

        while True:
            client.start_new_game()
            game = Game()

            while not game.complete:                
                client.show_board(game.board, False)
                move = client.get_move(game.current_player)

                if move == 'q':
                    self.leave_game(client)

                while not game.move_available(move):
                    client.move_already_taken()
                    move = client.get_move(game.current_player)

                    if move == 'q':
                        self.leave_game(client)

                game.process_turn(move)
                
            client.end_game(game.winner)
            client.show_board(game.board, True)

            if not client.play_again():
                self.leave_game(client)
            

if __name__ == "__main__":
    app = Application()
    app.run()
