from othello import Othello

#
# Main driver function to play the game from command line.
#
def main():
    print("!!!! WELCOME TO OTHELLO GAME !!!!\n")

    board_size = get_board_size()
    start_player = get_start_player()
    start_player_disc = get_start_player_disc()

    disc_colors = {Othello.BLACK: "BLACK", Othello.WHITE: "WHITE"}
    opponent_player = Othello.PLAYER1 if start_player == Othello.PLAYER2 else Othello.PLAYER2
    opponent_player_disc = Othello.BLACK if start_player_disc == Othello.WHITE else Othello.WHITE

    print(f"Othello Board Size: {board_size}")
    print(f"Player {start_player} with {disc_colors[start_player_disc]} disc")
    print(f"Player {opponent_player} with {disc_colors[opponent_player_disc]} disc")
    print(f"Player to start the game: Player {start_player}")

    game = Othello(board_size,start_player,start_player_disc)

    while not game.is_game_over():
        print(game)
        current_player = game.get_turn()
        current_player_disc = game.get_player_disc(current_player)
        if not game.is_a_valid_move_available(current_player_disc):
            print(f"No valid moves avaialable for player {current_player} ({disc_colors[current_player_disc]}). You lose your turn.")
            game.set_next_turn()
        else:
            while True:
                data = input(f"Player {current_player}'s Turn ({disc_colors[current_player_disc]}) - Where do you like to place the disc (row# col#)? ")
                row, col = data.split()
                row = int(row)
                col = int(col)
                if row < 0 or row >= board_size or col < 0 or col >= board_size:
                    print("Sorry, wrong input(s). Try again.")
                    continue
                if not game.is_valid_move(row,col,current_player_disc):
                    print("Sorry, that was not a valid move. Try again.")
                    continue
                break
            game.place_disc_at_pos(row,col,current_player_disc)

    print(game)
    winner = game.who_won()
    if winner == Othello.TIE:
        print("No winner - the game resulted in a tie.")
    else:
        print(f"Game over. The winner is player {winner} ({disc_colors[game.get_player_disc(winner)]})")


#
# Function that prompts and reads the board size information.
#
def get_board_size():
    while True:
        size = int(input("Enter board size (4 or 6 or 8): "))
        if size == 4 or size == 6 or size == 8:
            return size
        print("Invalid board size. Try again.")
        

#
# Function that prompts and reads which player starts the game.
#        
def get_start_player():
    while True:
        player = int(input("Enter player to start the game (1 or 2): "))
        if player == Othello.PLAYER1 or player == Othello.PLAYER2:
            return player
        print("Invalid player number. Try again.")


#
# Function that prompts and reads the disc color of the start player.
#
def get_start_player_disc():
    while True:
        disc = input("Enter disc color of start player (W/w or B/b): ").upper()
        if disc == Othello.BLACK or disc == Othello.WHITE:
            return disc
        print("Invalid input for disc color. Try again.")


#
#  Invoke main() if executed as a top-level script
#
if __name__ == "__main__":
    main()
    