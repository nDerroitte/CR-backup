# -*- coding: utf-8 -*-
        
class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0
        
    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1
    
    def score(self):
        
        currently_winning = self.p1N if self.p1 > self.p2 else self.p2N
        score = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        
        # Situation 1: . maximum score of 40 for everybody (p.1 and p.2 < 4)
        #              . not yet at 40-40 (p1 + p2 < 6)
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            return score[self.p1] + "-All" if (self.p1 == self.p2) else score[self.p1] + "-" + score[self.p2]
        
        # Situation 2: Either "Deuce", "Advantage" or "Win"
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            
            pointDiff = abs(self.p1-self.p2)
            return "Advantage " + currently_winning if (pointDiff == 1) else "Win for " + currently_winning
