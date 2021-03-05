from validators import Validator
from repo import Repo


class Service(object):
    def __init__(self):
        self.validator = Validator()
        self.repo = Repo()

    def position_player_boat(self, boat, row, col, orientation):
        # function that validates the given data, sets the positions of the boat and adds it on the bord
        self.validator.validate_position(row, col, orientation, boat)
        boat.set_position(row, col, orientation)
        self.repo.add_player_boat(boat)

    def position_computer_boat(self, boat, row, col, orientation):
        # function that validates the given data, sets the positions of the boat and adds it on the bord
        self.validator.validate_position(row, col, orientation, boat)
        boat.set_position(row, col, orientation)
        self.repo.add_computer_boat(boat)

    def player_attack(self, row, col):
        # function that validates the given data, and returns the status of the winner, adding meanwhile the attack on
        # the board
        self.validator.validate_attack(row, col)
        return self.repo.player_attack(row, col)

    def computer_attack(self, row, col):
        # function that validates the given data, and returns the status of the winner, adding meanwhile the attack on
        # the board
        self.validator.validate_attack(row, col)
        return self.repo.computer_attack(row, col)

    def get_player_board(self):
        # function that returns the player's board
        return self.repo.get_player_board()

    def get_computer_board(self):
        # function that returns the computer's board
        return self.repo.get_computer_board()
