# -*- coding: utf-8 -*-

class TennisGame1:
    def __init__(self, player1Name, player2Name):
    
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        self.RESULTS = ["Love", "Fifteen", "Thirty", "Forty", "Advantage "]

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1


    def current_winner(self):
        if self.p1points > self.p2points:
            return self.player1Name
        return self.player2Name

    def score(self):
        # Same score
        if self.p1points == self.p2points:
            # 3 points already : Deuce
            if self.p1points >= 3:
                return "Deuce"
            # All situation
            return self.RESULTS[self.p1points] + "-All"
         # Advantage or win for one player 
        elif self.p1points >= 4 or self.p2points >= 4:
            delta = abs(self.p1points - self.p2points)
            # Only one score difference : advantage
            if delta == 1:
                return "Advantage " + self.current_winner()
            # Win for player
            return "Win for " + self.current_winner()
        # Other situations
        return f"{self.RESULTS[self.p1points]}-{self.RESULTS[self.p2points]}"
