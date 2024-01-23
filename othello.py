class Othello(object):
    """Othello class implements the game logic of Othello board game."""

    # Useful constants - refer to these class attributes as Othello.attributename
    BLACK = 'B'     # access as Othello.BLACK
    WHITE = 'W'     # access as Othello.WHITE
    EMPTY = 'E'     # access as Othello.EMPTY
    PLAYER1 = 1     # access as Othello.PLAYER1
    PLAYER2 = 2     # access as Othello.PLAYER2
    TIE = 0         # access as Othello.TIE

    # DO NOT MAKE CHANGES TO THIS METHOD
    def __init__(self, board_size, start_player, start_player_disc):
        """
        Iniitializes Othello object's attributes as described below.

        Parameters:
            board_size: size of othello board
            start_player: player that starts the game
            start_player_disc: disc color of the start player

        Instance Attributes:
            self._size (int): initialized with the value of parameter board_size
            self._turn (int): initialized with the value of parameter start_player
            self._player1_disc (str): initialize it appropriately using the value of parameter start_player_disc
            self._player2_disc (str): initialize it appropriately using the value of parameter start_player_disc
            self._board (list of lists): game board initialized appropriately

        Validations and Exceptions:
            Raise ValueError if parameter board_size is not 4 or 6 or 8
            Raise ValueError if parameter start_player is < 1 or > 2
            Raise ValueError if parameter start_player_disc is not valid.
        """
        if board_size < 4 or board_size > 8 or board_size % 2 != 0:
            raise ValueError("Board size can only be 4 or 6 or 8.")
        if start_player < Othello.PLAYER1 or start_player > Othello.PLAYER2:
            raise ValueError("Player number is not valid.")
        if not (start_player_disc == Othello.BLACK or start_player_disc == Othello.WHITE):
            raise ValueError("Disc color is not valid.")

        self._size = board_size
        self._turn = start_player
        
        if start_player == Othello.PLAYER1:
            self._player1_disc = start_player_disc
            self._player2_disc = Othello.WHITE if start_player_disc == Othello.BLACK else Othello.BLACK
        else:
            self._player2_disc = start_player_disc
            self._player1_disc = Othello.WHITE if start_player_disc == Othello.BLACK else Othello.BLACK

        self._board = []

        # Setup the board to initial game board configuration
        for i in range(self._size):
            self._board.append([Othello.EMPTY] * self._size)
        pos = (self._size - 2) // 2
        self._board[pos][pos] = Othello.BLACK
        self._board[pos][pos+1] = Othello.WHITE
        self._board[pos+1][pos] = Othello.WHITE
        self._board[pos+1][pos+1] = Othello.BLACK


    def get_board_size(self):
        """Returns the board size."""
        return self._size


    def get_turn(self):
        """Returns the current value of self._turn indicating whose turn it is currently."""
        return self._turn


    def set_next_turn(self):
        """Sets the value of self._turn to next player."""
        self._turn = Othello.PLAYER1 if self._turn == Othello.PLAYER2 else Othello.PLAYER2


    def get_player_disc(self, player):
        """
        Return the disc of player indicated by parameter player.

        Parameter:
            player (int): player number whose disc is returned

        Validations and Exceptions:
            Raise ValueError if parameter player is < 1 or > 2
        """
        if player < Othello.PLAYER1 or player > Othello.PLAYER2:
            raise ValueError("Player number is not valid.")
        if player == Othello.PLAYER1:
            return self._player1_disc
        else:
            return self._player2_disc


    def is_valid_move(self, row, col, disc):
        """
        Return True if placing the disc at location row,col is valid; False otherwise.

        Parameters:
            row (int): row number (0-based index)
            col (int): column number (0-based index)
            disc (str): disc color
       
        Validations and Exceptions:
            Return False if row and/or col values is not within the bounds of the board.
            Raises ValueError if the value of parameter disc is not valid.
        """
        if row < 0 or col < 0 or row > (self.get_board_size()-1) or col > (self.get_board_size()-1):
            return False
        if not (disc == Othello.BLACK or disc == Othello.WHITE):
            raise ValueError("Disc color is not valid.")
        if self._board[row][col] != Othello.EMPTY:
            return False
        steps = [-1, 0, 1]
        for i in steps:
            for j in steps:
                if i == 0 and j == 0:
                    continue
                r = row + i
                c = col + j
                if r < 0 or r > (self.get_board_size()-1) or c < 0 or c > (self.get_board_size()-1):
                    continue
                if self._board[r][c] == disc:
                    continue
                while self._board[r][c] != Othello.EMPTY:
                    r += i
                    c += j
                    if r < 0 or r > (self.get_board_size()-1) or c < 0 or c > (self.get_board_size()-1):
                        break
                    if self._board[r][c] == disc:
                        return True
        return False

    
    # DO NOT MAKE CHANGES TO THIS METHOD
    def is_a_valid_move_available(self, disc):
        """
        Return True if a valid move for disc is available; False otherwise.

        Parameter:
            disc (str): disc color
        """
        # check if a valid move is available
        for i in range(self._size):
            for j in range(self._size):
                if self.is_valid_move(i,j,disc):
                    return True
        return False


    def place_disc_at_pos(self, row, col, disc):
        """
        Place the disc at location row,col on the board, if valid.

        Parameters:
            row (int): row number (0-index based)
            col (int): column number (0-index based)
            disc (str): disc color
       
        Validations and Exceptions:
            Return None if placement of disc at location row,col is not valid (use is_valid_move() to check this).
        """
        if self.is_valid_move(row, col, disc):
            self._board[row][col] = disc
            steps = [-1, 0, 1]
            main = []
            for i in steps:
                for j in steps:
                    temp = []
                    if i == 0 and j == 0:
                        continue
                    r = row + i
                    c = col + j
                    if r < 0 or r > (self.get_board_size()-1) or c < 0 or c > (self.get_board_size()-1):
                        continue
                    if self._board[r][c] == disc:
                        continue
                    while self._board[r][c] != Othello.EMPTY:
                        temp.append([r, c])
                        r += i
                        c += j
                        if r < 0 or r > (self.get_board_size()-1) or c < 0 or c > (self.get_board_size()-1):
                            break
                        if self._board[r][c] == disc:
                            for ind in temp:
                                self._board[ind[0]][ind[1]] = disc
                            break

        # DO NOT MAKE CHANGES TO THE CODE BELOW
        if not self.is_game_over():
            self.set_next_turn()


    def is_board_full(self):
        """Returns True if the board is full; False otherwise."""
        for i in self._board:
            for j in i:
                if j == Othello.EMPTY:
                    return False
        return True


    def is_game_over(self):
        """Returns True if the game is over; False otherwise."""
        # current_player = self.get_turn()
        # current_disc = self.get_player_disc(current_player)
        # if self.is_a_valid_move_available(current_disc):
        #     return False
        # else:
        #     return True
        if self.is_board_full():
            return True
        
        return False


    def who_won(self):
        """
        If game is over, return the player number that won the game. In case of a tie, return
        Othello.TIE. Return None if game is not over.
        """
        if self.is_game_over():
            w = 0
            b = 0
            for i in self._board:
                for j in i:
                    if j == Othello.WHITE:
                        w+=1
                    elif j == Othello.BLACK:
                        b+=1
            if w == b:
                return Othello.TIE
            elif w > b:
                if self._player1_disc == Othello.WHITE:
                    return Othello.PLAYER1
                else:
                    return Othello.PLAYER2
            else:
                if self._player1_disc == Othello.BLACK:
                    return Othello.PLAYER1
                else:
                    return Othello.PLAYER2


    # DO NOT MAKE CHANGES TO THIS METHOD
    def __repr__(self):
        """Returns printable representation of Othello object."""
        result_str = "\n  "
        for i in range(self._size):
            result_str += str(i) + " "
        result_str = result_str.rstrip() + "\n"
        for i in range(self._size):
            result_str += str(i) + " "
            for j in range(self._size):
                if self._board[i][j] == Othello.WHITE:
                    result_str += "W "
                elif self._board[i][j] == Othello.BLACK:
                    result_str += "B "
                else:
                    result_str += "- "
            result_str = result_str.rstrip() + "\n"  
        return result_str 

