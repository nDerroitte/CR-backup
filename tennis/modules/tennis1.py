# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        if (self.p1points == self.p2points):
            if self.p1points < 3:
                result = {
                    0: "Love-All",
                    1: "Fifteen-All",
                    2: "Thirty-All",
                }[self.p1points]
            else:
                result = "Deuce"
        elif (self.p1points >= 4 or self.p2points >= 4):
            if (self.p1points == self.p2points + 1):
                result = "Advantage " + self.player1Name
            elif (self.p2points == self.p1points + 1):
                result = "Advantage " + self.player2Name
            elif (self.p1points > self.p2points + 1):
                result = "Win for " + self.player1Name
            else:
                result = "Win for " + self.player2Name
        else:
            conversion = {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }
            result = conversion[self.p1points] + "-" + conversion[self.p2points]
        return result
