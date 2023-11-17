# -*- coding: utf-8 -*-
class TennisGame2:
    scoremax =4
    deuceValue=6

    #function called when we create an object of the class
    def __init__(self, player1Name, player2Name):
        self.p1Name = player1Name
        self.p2Name = player2Name
        self.p1Score = 0
        self.p2Score = 0


    #function used to know which player has won the point
    def won_point(self, n):
        if n == self.p1Name:
            self.p1Score += 1
        else:
            self.p2Score += 1
    #function used to display the score
    def score(self):
        if (self.p1Score < self.scoremax and self.p2Score < self.scoremax) and (self.p1Score + self.p2Score < self.deuceValue):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            #return score playerOne and all if they have the same score otherwise the two score are displayed
            return p[self.p1Score] + "-All" if (self.p1Score == self.p2Score) else p[self.p1Score] + "-" + p[self.p2Score]
        else:
            if (self.p1Score == self.p2Score):
                return "Deuce"
            return self.scoreadv_final()


    #function to manage the advantage or the final score
    def scoreadv_final(self):
        if self.p1Score > self.p2Score:
            #if the difference is greater than on it means that there is a winner
            if self.p1Score-self.p2Score>1:
                return "Win for " + self.p1Name
            return "Advantage " + self.p1Name
        else:
            if self.p2Score - self.p1Score > 1:
                return "Win for " + self.p2Name
            return "Advantage " + self.p2Name