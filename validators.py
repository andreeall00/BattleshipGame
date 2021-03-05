from errors import ValidError


class Validator(object):
    def __init__(self):
        pass

    def validate_position(self, row, col, orientation, boat):
        errors = ""
        if row < 0 or row > 7:
            errors += "Invalid row! Please choose a nr from 0 to 7\n"
        if col < 0 or col > 7:
            errors += "Invalid column! Please choose a nr from 0 to 7\n"
        if orientation != 'v' and orientation != 'h':
            errors += "Invalid orientation! Please write v for vertical or h for horizontal\n"
        if (orientation == 'v' and row + boat.get_size() - 1 > 7) or (orientation == 'h' and col + boat.get_size() - 1 > 7):
            errors += "Invalid position! The boat is outside the board\n"
        if len(errors) > 0:
            raise ValidError(errors)

    def validate_attack(self, row, col):
        errors = ""
        if row < 0 or row > 7:
            errors += "Invalid row! Please choose a nr from 0 to 7\n"
        if col < 0 or col > 7:
            errors += "Invalid column! Please choose a nr from 0 to 7\n"
        if len(errors) > 0:
            raise ValidError(errors)
