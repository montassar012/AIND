"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = sample_players.GreedyPlayer(sample_players.improved_score)
        self.player3 = game_agent.AlphaBetaPlayer()
       # self.game = isolation.Board(self.player1, self.player2,7,7)
        self.game = isolation.Board(self.player2, self.player3,7,7)
    def test_example(self):
        print("starting game")

        winner, history, outcome =self.game.play(2000)
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
