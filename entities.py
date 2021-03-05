class Boat:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.row = None
        self.col = None
        self.orientation = None

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_orientation(self):
        return self.orientation

    def set_position(self, row, col, orientation):
        self.row = row
        self.col = col
        self.orientation = orientation


class Board:
    def __init__(self):
        self.grid = [[" _", " _", " _", " _", " _", " _", " _", " _"],
                     [" _", " _", " _", " _", " _", " _", " _", " _"],
                     [" _", " _", " _", " _", " _", " _", " _", " _"],
                     [" _", " _", " _", " _", " _", " _", " _", " _"],
                     [" _", " _", " _", " _", " _", " _", " _", " _"],
                     [" _", " _", " _", " _", " _", " _", " _", " _"],
                     [" _", " _", " _", " _", " _", " _", " _", " _"],
                     [" _", " _", " _", " _", " _", " _", " _", " _"]
                     ]
        self.hit_count = 0

    def set_grid(self, row, col, symbol):
        self.grid[row][col] = symbol

    def set_hit_count(self, nr):
        self.hit_count = nr

    def get_hit_count(self):
        return self.hit_count

    def get_grid(self):
        return self.grid

    # The function converts the grid to a string representation for printing
    def get_visible_view(self):
        str_val = "  0 1 2 3 4 5 6 7\n"
        for i in range(8):
            str_val += str(i)
            for j in range(8):
                str_val += self.grid[i][j]
            if i != 7:
                str_val += "\n"
        return str_val

    # The function converts the grid to a string representation with boat locations hidden
    def get_hidden_view(self):
        str_val = "  0 1 2 3 4 5 6 7\n"
        for i in range(8):
            str_val += str(i)
            for j in range(8):
                if self.grid[i][j] == " B":
                    str_val += " _"
                else:
                    str_val += self.grid[i][j]
            if i != 7:
                str_val += "\n"
        return str_val
