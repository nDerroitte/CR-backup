# -*- coding: utf-8 -*-
        
class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1 = player1Name
        self.player2 = player2Name
        self.point_player1 = 0
        self.point_player2 = 0
        
    def won_point(self, n):
        if n == self.player1:
            self.point_player1 += 1
        else:
            self.point_player2 += 1
    
    def score(self):
        
        currently_winning = self.player1 if self.point_player1 > self.point_player2 else self.player2
        score = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        
        # Situation 1: . maximum score of 40 for everybody (p.1 and p.2 < 4)
        #              . not yet at 40-40 (p1 + p2 < 6)
        if (self.point_player1 < 4 and self.point_player2 < 4) and (self.point_player1 + self.point_player2 < 6):
            return score[self.point_player1] + "-All" if (self.point_player1 == self.point_player2) else score[self.point_player1] + "-" + score[self.point_player2]
        
        # Situation 2: Either "Deuce", "Advantage" or "Win"
        else:
            if (self.point_player1 == self.point_player2):
                return "Deuce"
            
            pointDiff = abs(self.point_player1-self.point_player2)
            return "Advantage " + currently_winning if (pointDiff == 1) else "Win for " + currently_winning
