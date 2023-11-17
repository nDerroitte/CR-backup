# -*- coding: utf-8 -*-

from modules.tennis1 import TennisGame1

players = ["Nadal", "Federer"]
 
if __name__ == "__main__":
    p1, p2 = players
    game = TennisGame1(p1, p2)
    print("Start of the game.")
    print("---")
    # 0 - 0
    print(game.score())
    game.won_point(p2)
    print(game.score())
    # 0 - 15
    game.won_point(p2)
    print(game.score())
    # 0 - 30
    game.won_point(p2)
    print(game.score())
    # 0 - 40
    game.won_point(p1)
    print(game.score())
    # 15 - 40
    game.won_point(p2)
    print(game.score())
    # Win P2
    print("---")

