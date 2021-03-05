from entities import Boat
from service import Service
from errors import RepositoryError, ValidError
from random import randint
import random
from tests import Tests


class Play(object):
    def __init__(self):
        self.service = Service()
        self.fleet = [Boat("battleship", 4), Boat("cruiser", 3), Boat("destroyer", 2)]

    def __ui_player_position_fleet(self):
        print("Position your fleet")
        for boat in self.fleet:
            print(self.service.get_player_board())
            print("Position the", boat.get_name(), "of length", boat.get_size())
            position = None
            while position is None:
                try:
                    position = input("Please enter the position for the top-left location of the boat(use the form: row"
                                     ",col,orientation(v-vertical, h-horizontal)): ")
                    pos = position.split(",")
                    row = int(pos[0].strip())
                    col = int(pos[1].strip())
                    orientation = pos[2].strip()
                    self.service.position_player_boat(boat, row, col, orientation)
                except ValueError as ve:
                    print("UI Error: " + str(ve))
                    position = None
                except ValidError as vde:
                    print("Service Error: " + str(vde))
                    position = None
                except RepositoryError as re:
                    print("Repository Error: " + str(re))
                    position = None
                except IndexError:
                    print("UI Error: Incomplete position!\n")
                    position = None

    def __ui_computer_position_fleet(self):
        for boat in self.fleet:
            position = None
            while position is None:
                try:
                    orientation = ['v', 'h']
                    position = [randint(0, 7), randint(0, 7), random.choice(orientation)]
                    row = position[0]
                    col = position[1]
                    orientation = position[2]
                    self.service.position_computer_boat(boat, row, col, orientation)
                except ValueError:
                    position = None
                except ValidError:
                    position = None
                except RepositoryError:
                    position = None

    def __ui_player_turn(self):
        position = None
        while position is None:
            try:
                position = input("The position you would like to attack(use the form: row,col): ")
                position = position.split(",")
                row = int(position[0].strip())
                col = int(position[1].strip())
                winner = self.service.player_attack(row, col)
                if winner:
                    return True
                else:
                    return False
            except ValueError as ve:
                print("UI Error: " + str(ve))
                position = None
            except ValidError as vde:
                print("Service Error: " + str(vde))
                position = None
            except RepositoryError as re:
                print("Repository Error: " + str(re))
                position = None
            except IndexError:
                print("UI Error: Incomplete position!\n")
                position = None

    def __ui_computer_turn(self):
        position = None
        while position is None:
            try:
                position = [randint(0, 7), randint(0, 7)]
                row = position[0]
                col = position[1]
                winner = self.service.computer_attack(row, col)
                if winner:
                    return True
                else:
                    return False
            except ValueError:
                position = None
            except ValidError:
                position = None
            except RepositoryError:
                position = None

    def play(self):
        print("-----Battleship-----")
        self.__ui_computer_position_fleet()
        self.__ui_player_position_fleet()
        print("Let's play!")
        winner = False
        turn = True
        while not winner:
            if turn:
                print("Your turn: ")
                winner = self.__ui_player_turn()
                if winner:
                    print("You won!")
            else:
                winner = self.__ui_computer_turn()
                print(self.service.get_player_board())
                print(self.service.get_computer_board())
                if winner:
                    print("You lost!")
            turn = not turn


Tests().run_all()
Play().play()
