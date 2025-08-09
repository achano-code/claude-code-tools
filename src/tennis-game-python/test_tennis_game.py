import unittest
from tennis_game import TennisGame

class TestTennisGame(unittest.TestCase):
    def setUp(self):
        self.game = TennisGame("Alice", "Bob")
    
    def test_initial_score(self):
        self.assertEqual(self.game.get_score(), "Love-Love")
    
    def test_player1_wins_first_ball(self):
        self.game.win_ball("Alice")
        self.assertEqual(self.game.get_score(), "Fifteen-Love")
    
    def test_player2_wins_first_ball(self):
        self.game.win_ball("Bob")
        self.assertEqual(self.game.get_score(), "Love-Fifteen")
    
    def test_player1_wins_first_two_balls(self):
        self.game.win_ball("Alice")
        self.game.win_ball("Alice")
        self.assertEqual(self.game.get_score(), "Thirty-Love")
    
    def test_player1_wins_first_three_balls(self):
        self.game.win_ball("Alice")
        self.game.win_ball("Alice")
        self.game.win_ball("Alice")
        self.assertEqual(self.game.get_score(), "Forty-Love")
    
    def test_deuce_scenario(self):
        for _ in range(3):
            self.game.win_ball("Alice")
            self.game.win_ball("Bob")
        self.assertEqual(self.game.get_score(), "Deuce")
    
    def test_advantage_player1(self):
        for _ in range(3):
            self.game.win_ball("Alice")
            self.game.win_ball("Bob")
        self.game.win_ball("Alice")
        self.assertEqual(self.game.get_score(), "Advantage Alice")
    
    def test_advantage_player2(self):
        for _ in range(3):
            self.game.win_ball("Alice")
            self.game.win_ball("Bob")
        self.game.win_ball("Bob")
        self.assertEqual(self.game.get_score(), "Advantage Bob")
    
    def test_player1_wins_game(self):
        for _ in range(4):
            self.game.win_ball("Alice")
        self.assertEqual(self.game.get_score(), "Win for Alice")
    
    def test_player2_wins_game(self):
        for _ in range(4):
            self.game.win_ball("Bob")
        self.assertEqual(self.game.get_score(), "Win for Bob")
    
    def test_win_from_deuce(self):
        for _ in range(3):
            self.game.win_ball("Alice")
            self.game.win_ball("Bob")
        self.game.win_ball("Alice")
        self.game.win_ball("Alice")
        self.assertEqual(self.game.get_score(), "Win for Alice")

if __name__ == "__main__":
    unittest.main()