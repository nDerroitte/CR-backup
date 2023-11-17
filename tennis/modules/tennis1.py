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

    def _parity_scenarios(self):
        if self.p1points < 3:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }[self.p1points]
        else:
            result = "Deuce"
        return result

    def _classic_scenario(self):
        conversion = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        result = conversion[self.p1points] + "-" + conversion[self.p2points]
        return result

    def _advantage_and_victory_scenario(self):
        if (self.p1points == self.p2points + 1):
            result = "Advantage " + self.player1Name
        elif (self.p2points == self.p1points + 1):
            result = "Advantage " + self.player2Name
        elif (self.p1points > self.p2points + 1):
            result = "Win for " + self.player1Name
        else:
            result = "Win for " + self.player2Name
        return result

    def score(self):
        result = ""
        if (self.p1points == self.p2points):
            result = self._parity_scenarios()
        elif (self.p1points >= 4 or self.p2points >= 4):
            result = self._advantage_and_victory_scenario()
        else:
            result = self._classic_scenario()
        return result
