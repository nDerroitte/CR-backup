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

    def who_won(self):
        if self.p1points > self.p2points:
            return self.player1Name
        else:
            return self.player2Name

    def score(self):
        result = ""
        tempScore=0
        if (self.p1points==self.p2points):
            p = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce", "Deuce"]
            result = p[self.p2points]
        elif (self.p1points>=4 or self.p2points>=4):
            if (abs(self.p1points-self.p2points)==1): # if advantage
                result ="Advantage " + self.who_won()
            else:
                result ="Win for " + self.who_won()
        else:
            for i in range(1,3):
                if (i==1):
                    tempScore = self.p1points
                else:
                    result+="-"
                    tempScore = self.p2points
                result += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[tempScore]
        return result