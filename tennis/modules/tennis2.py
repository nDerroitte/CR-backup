# -*- coding: utf-8 -*-
        
class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1 = player1Name
        self.player2 = player2Name
        self.points_player1 = 0
        self.points_player2 = 0
        self.RESULT = ["Love", "Fifteen", "Thirty", "Forty"]
        
    def won_point(self, playerName):
        if playerName == self.player1:
            self.points_player1 += 1
        else:
            self.points_player2 += 1
    
    def current_winner(self):
        if self.points_player1 > self.points_player2:
            return self.player1
        else:
            return self.player2

    
    def score(self):
        #Same score 
        if (self.points_player1 == self.points_player2):
            if self.points_player1 < 3:
                return self.RESULT[self.points_player1] + "-All"
            else:
                return "Deuce"

        #Nobody won and we didn't get to advantages yet
        PointsUnder4 = (self.points_player1 < 4 and self.points_player2 < 4)
        if PointsUnder4: 
           score_player1 = self.RESULT[self.points_player1]
           score_player2 = self.RESULT[self.points_player2]
           return score_player1 + "-" + score_player2
           
        #Advantage or Win
        else:
            if abs(self.points_player1 - self.points_player2) == 1:
                return "Advantage " + self.current_winner()
            else:
                return "Win for " + self.current_winner()
