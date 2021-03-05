from entities import Board
from errors import RepositoryError


class Repo(object):
    def __init__(self):
        self.player_board = Board()
        self.computer_board = Board()

    def add_player_boat(self, boat):
        # function that adds a boat on the player's board, and raises an error if there already exists a boat there
        if boat.get_orientation() == 'h':
            for pos in range(boat.get_col(), boat.get_col() + boat.get_size()):
                if self.player_board.get_grid()[boat.get_row()][pos] != " _":
                    raise RepositoryError("There already exists a boat here!\n")
            for pos in range(boat.get_col(), boat.get_col() + boat.get_size()):
                self.player_board.get_grid()[boat.get_row()][pos] = " B"

        if boat.get_orientation() == 'v':
            for pos in range(boat.get_row(), boat.get_row() + boat.get_size()):
                if self.player_board.get_grid()[pos][boat.get_col()] != " _":
                    raise RepositoryError("There already exists a boat here!\n")
            for pos in range(boat.get_row(), boat.get_row() + boat.get_size()):
                self.player_board.get_grid()[pos][boat.get_col()] = " B"

    def add_computer_boat(self, boat):
        # function that adds a boat on the player's board, and raises an error if there already exists a boat there
        if boat.get_orientation() == 'h':
            for pos in range(boat.get_col(), boat.get_col() + boat.get_size()):
                if self.computer_board.get_grid()[boat.get_row()][pos] != " _":
                    raise RepositoryError("There already exists a boat here!\n")
            for pos in range(boat.get_col(), boat.get_col() + boat.get_size()):
                self.computer_board.get_grid()[boat.get_row()][pos] = " B"

        if boat.get_orientation() == 'v':
            for pos in range(boat.get_row(), boat.get_row() + boat.get_size()):
                if self.computer_board.get_grid()[pos][boat.get_col()] != " _":
                    raise RepositoryError("There already exists a boat here!\n")
            for pos in range(boat.get_row(), boat.get_row() + boat.get_size()):
                self.computer_board.get_grid()[pos][boat.get_col()] = " B"

    def player_attack(self, row, col):
        # function that raises an error if the square has already been attacked, and if not, it adds the attack on the
        # board, X - if it hit a boat, O - if it didn't
        if self.computer_board.get_grid()[row][col] == ' X' or self.computer_board.get_grid()[row][col] == ' O':
            raise RepositoryError("You already attacked here!\n")

        if self.computer_board.get_grid()[row][col] == ' B':
            self.computer_board.set_grid(row, col, ' X')
            self.player_board.set_hit_count(self.player_board.get_hit_count() + 1)
        elif self.computer_board.get_grid()[row][col] == ' _':
            self.computer_board.set_grid(row, col, ' O')

        if self.player_board.get_hit_count() == 9:
            return True
        else:
            return False

    def computer_attack(self, row, col):
        # function that raises an error if the square has already been attacked, and if not, it adds the attack on the
        # board, X - if it hit a boat, O - if it didn't
        if self.player_board.get_grid()[row][col] == ' X' or self.player_board.get_grid()[row][col] == ' O':
            raise RepositoryError("You already attacked here!\n")

        if self.player_board.get_grid()[row][col] == ' B':
            self.player_board.set_grid(row, col, ' X')
            self.computer_board.set_hit_count(self.computer_board.get_hit_count() + 1)
        elif self.player_board.get_grid()[row][col] == ' _':
            self.player_board.set_grid(row, col, ' O')

        if self.computer_board.get_hit_count() == 9:
            return True
        else:
            return False

    def get_player_board(self):
        # function that returns the player's board
        return self.player_board.get_visible_view()

    def get_computer_board(self):
        # function that returns the computer's board
        return self.computer_board.get_hidden_view()
