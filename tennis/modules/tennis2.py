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
        points = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}
        if (self.points_player1 < 4 and self.points_player2 < 4) and (self.points_player1 + self.points_player2 < 6):
           score_player1 = points[self.points_player1]
           score_player2 = points[self.points_player2]
           if (self.points_player1 == self.points_player2):
               return score_player1 + "-All"
           else:
               return score_player1 + "-" + score_player2
        else:
            if (self.points_player1 == self.points_player2):
                return "Deuce"
            score = self.player1 if self.points_player1 > self.points_player2 else self.player2
            return "Advantage " + score if ((self.points_player1-self.points_player2)*(self.points_player1-self.points_player2) == 1) else "Win for " + score
