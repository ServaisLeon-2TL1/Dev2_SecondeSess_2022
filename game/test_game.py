
import unittest
import game


class TestTerrain(unittest.TestCase):

    def test_default_vertical_win_p1(self):
        game_ = game.Game()
        stein = game_.players[0].symbol
        game_.terrain.occupied_positions[(0, 3)] = stein
        game_.terrain.occupied_positions[(0, 2)] = stein
        game_.terrain.occupied_positions[(0, 1)] = stein
        game_.terrain.occupied_positions[(0, 0)] = stein
        self.assertTrue(game_.check_winner(stein))

    def test_default_horizontal_win_p1(self):
        game_ = game.Game()
        stein = game_.players[0].symbol
        game_.terrain.occupied_positions[(0, 3)] = stein
        game_.terrain.occupied_positions[(1, 3)] = stein
        game_.terrain.occupied_positions[(2, 3)] = stein
        game_.terrain.occupied_positions[(3, 3)] = stein
        self.assertTrue(game_.check_winner(stein))

    def test_default_diagonal_rl_win_p1(self):
        game_ = game.Game()
        stein = game_.players[0].symbol
        game_.terrain.occupied_positions[(0, 3)] = stein
        game_.terrain.occupied_positions[(1, 2)] = stein
        game_.terrain.occupied_positions[(2, 1)] = stein
        game_.terrain.occupied_positions[(3, 0)] = stein
        self.assertTrue(game_.check_winner(stein))

    def test_default_diagonal_lf_win_p1(self):
        game_ = game.Game()
        stein = game_.players[0].symbol
        game_.terrain.occupied_positions[(3, 3)] = stein
        game_.terrain.occupied_positions[(2, 2)] = stein
        game_.terrain.occupied_positions[(1, 1)] = stein
        game_.terrain.occupied_positions[(0, 0)] = stein
        self.assertTrue(game_.check_winner(stein))

    def test_default_not_win_p1_empty(self):
        field = game.Terrain()
        stein = field.players[0].symbol
        self.assertFalse(field.check_winner(stein))

    def test_default_not_win_p2_empty(self):
        field = game.Terrain()
        stein = field.players[1].symbol
        self.assertFalse(field.check_winner(stein))

    def test_default_vertical_not_win_p1_partial_1(self):
        field = game.Terrain()
        stein = field.players[0].symbol
        field.terrain[(0, 3)] = stein
        self.assertFalse(field.check_winner(stein))

    def test_default_vertical_not_win_p1_partial_2(self):
        field = game.Terrain()
        stein = field.players[0].symbol
        field.terrain[(0, 3)] = stein
        field.terrain[(0, 2)] = stein
        field.terrain[(0, 1)] = stein
        self.assertFalse(field.check_winner(stein))