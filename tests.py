import unittest
from service import Service
from entities import Boat


class Tests(unittest.TestCase):
    def test_position_player_boat(self):
        service = Service()
        self.boat = Boat("battleship", 4)
        self.assertRaises(Exception, lambda: service.position_player_boat(Boat("battleship", 4), -1, 2, 'v'))
        self.assertRaises(Exception, lambda: service.position_player_boat(Boat("battleship", 4), 1, -2, 'v'))
        self.assertRaises(Exception, lambda: service.position_player_boat(Boat("battleship", 4), 1, 2, 'a'))
        self.assertRaises(Exception, lambda: service.position_player_boat(Boat("battleship", 4), -1, -2, 'a'))
        service.position_player_boat(self.boat, 1, 2, 'v')
        self.assertEqual(1, self.boat.get_row())
        self.assertEqual(2, self.boat.get_col())
        self.assertEqual('v', self.boat.get_orientation())
        self.assertRaises(Exception, lambda: service.position_player_boat(self.boat, 2, 2, 'v'))

    def test_player_attack(self):
        service = Service()
        self.assertRaises(Exception, lambda: service.player_attack(-1, 0))
        self.assertRaises(Exception, lambda: service.player_attack(1, 8))
        self.assertRaises(Exception, lambda: service.player_attack(1, 'a'))
        service.player_attack(1, 1)
        self.assertRaises(Exception, lambda: service.player_attack(1, 1))
        self.assertEqual(False, service.player_attack(2, 3))

    def test_get_player_boat(self):
        service = Service()
        self.assertEqual("  0 1 2 3 4 5 6 7\n0 _ _ _ _ _ _ _ _\n1 _ _ _ _ _ _ _ _\n2 _ _ _ _ _ _ _ _\n3 _ _ _ _ _ _ _ _"
                         "\n4 _ _ _ _ _ _ _ _\n5 _ _ _ _ _ _ _ _\n6 _ _ _ _ _ _ _ _\n7 _ _ _ _ _ _ _ _",
                         service.get_player_board())
        service.position_player_boat(Boat("destroyer", 2), 0, 0, 'h')
        self.assertEqual("  0 1 2 3 4 5 6 7\n0 B B _ _ _ _ _ _\n1 _ _ _ _ _ _ _ _\n2 _ _ _ _ _ _ _ _\n3 _ _ _ _ _ _ _ _"
                         "\n4 _ _ _ _ _ _ _ _\n5 _ _ _ _ _ _ _ _\n6 _ _ _ _ _ _ _ _\n7 _ _ _ _ _ _ _ _",
                         service.get_player_board())

    def test_position_computer_boat(self):
        service = Service()
        self.boat = Boat("battleship", 4)
        self.assertRaises(Exception, lambda: service.position_computer_boat(Boat("battleship", 4), -1, 2, 'v'))
        self.assertRaises(Exception, lambda: service.position_computer_boat(Boat("battleship", 4), 1, -2, 'v'))
        self.assertRaises(Exception, lambda: service.position_computer_boat(Boat("battleship", 4), 1, 2, 'a'))
        self.assertRaises(Exception, lambda: service.position_computer_boat(Boat("battleship", 4), -1, -2, 'a'))
        service.position_computer_boat(self.boat, 1, 2, 'v')
        self.assertEqual(1, self.boat.get_row())
        self.assertEqual(2, self.boat.get_col())
        self.assertEqual('v', self.boat.get_orientation())
        self.assertRaises(Exception, lambda: service.position_computer_boat(self.boat, 2, 2, 'v'))

    def test_computer_attack(self):
        service = Service()
        self.assertRaises(Exception, lambda: service.computer_attack(-1, 0))
        self.assertRaises(Exception, lambda: service.computer_attack(1, 8))
        self.assertRaises(Exception, lambda: service.computer_attack(1, 'a'))
        service.computer_attack(1, 1)
        self.assertRaises(Exception, lambda: service.computer_attack(1, 1))
        self.assertEqual(False, service.computer_attack(2, 3))
        self.assertEqual(False, service.computer_attack(2, 2))

    def test_get_computer_boat(self):
        service = Service()
        self.assertEqual("  0 1 2 3 4 5 6 7\n0 _ _ _ _ _ _ _ _\n1 _ _ _ _ _ _ _ _\n2 _ _ _ _ _ _ _ _\n3 _ _ _ _ _ _ _ _"
                         "\n4 _ _ _ _ _ _ _ _\n5 _ _ _ _ _ _ _ _\n6 _ _ _ _ _ _ _ _\n7 _ _ _ _ _ _ _ _",
                         service.get_computer_board())
        service.position_computer_boat(Boat("destroyer", 2), 0, 0, 'h')
        self.assertEqual("  0 1 2 3 4 5 6 7\n0 _ _ _ _ _ _ _ _\n1 _ _ _ _ _ _ _ _\n2 _ _ _ _ _ _ _ _\n3 _ _ _ _ _ _ _ _"
                         "\n4 _ _ _ _ _ _ _ _\n5 _ _ _ _ _ _ _ _\n6 _ _ _ _ _ _ _ _\n7 _ _ _ _ _ _ _ _",
                         service.get_computer_board())
        service.player_attack(0, 0)
        self.assertEqual("  0 1 2 3 4 5 6 7\n0 X _ _ _ _ _ _ _\n1 _ _ _ _ _ _ _ _\n2 _ _ _ _ _ _ _ _\n3 _ _ _ _ _ _ _ _"
                         "\n4 _ _ _ _ _ _ _ _\n5 _ _ _ _ _ _ _ _\n6 _ _ _ _ _ _ _ _\n7 _ _ _ _ _ _ _ _",
                         service.get_computer_board())

    def run_all(self):
        self.test_position_player_boat()
        self.test_player_attack()
        self.test_get_player_boat()
        self.test_position_computer_boat()
        self.test_computer_attack()
        self.test_get_computer_boat()
