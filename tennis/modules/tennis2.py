# -*- coding: utf-8 -*-
        
class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1 = player1Name
        self.player2 = player2Name
        self.points_player1 = 0
        self.points_player2 = 0
        
    def won_point(self, playerName):
        if playerName == self.player1:
            self.points_player1 += 1
        else:
            self.points_player2 += 1
    
    def score(self):
        if (self.points_player1 < 4 and self.points_player2 < 4) and (self.p1 + self.p2 < 6):
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            score = points[self.points_player1]
            return score + "-All" if (self.points_player1 == self.points_player2) else s + "-" + points[self.points_player2]
        else:
            if (self.points_player1 == self.points_player2):
                return "Deuce"
            score = self.player1 if self.points_player1 > self.points_player2 else self.player2
            return "Advantage " + score if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + score
