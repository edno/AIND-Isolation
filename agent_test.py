"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import timeit

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)

    # def test_runminimax(self):
    #     print("MiniMax")
    #     self.player1 = game_agent.MinimaxPlayer()
    #     self.player1.name = "Player 1"
    #     self.player2 = game_agent.MinimaxPlayer()
    #     self.player2.name = "Player 2"
    #     self.game = isolation.Board(self.player1, self.player2)
    #     self.game.apply_move((1, 1))
    #     self.game.apply_move((6, 6))
    #     winner, history, result = self.game.play()
    #     print(winner.name, ",", self.game.move_count, ",", history, ",", result)
    #     print(self.game.to_string())

    # def test_runalphabeta(self):
    #     print("AlphaBeta 1")
    #     self.player1 = game_agent.AlphaBetaPlayer()
    #     self.player1.name = "Player 1"
    #     self.player2 = game_agent.AlphaBetaPlayer()
    #     self.player2.name = "Player 2"
    #     self.game = isolation.Board(self.player1, self.player2)
    #     self.game.apply_move((1, 1))
    #     self.game.apply_move((6, 6))
    #     winner, history, result = self.game.play()
    #     print(winner.name, ",", self.game.move_count, ",", history, ",", result)
    #     print(self.game.to_string())

    def test_runalphabeta2(self):
        results = {'Player 1': 0, 'Player 2': 0}

        for n in range(0, 10):
            # print("AlphaBeta 2")
            self.player1 = game_agent.AlphaBetaPlayer(score_fn=game_agent.custom_score_2)
            self.player1.name = "Player 1"
            self.player2 = game_agent.AlphaBetaPlayer(score_fn=game_agent.custom_score_2)
            self.player2.name = "Player 2"
            self.game = isolation.Board(self.player1, self.player2)
            self.game.apply_move((0, 0))
            self.game.apply_move((4, 4))
            winner, history, result = self.game.play()
            print(winner.name, ":", history)
            results[winner.name] += 1

        print(results)


if __name__ == '__main__':
    unittest.main()
