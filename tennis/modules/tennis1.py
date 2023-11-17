# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.tempscore = 0
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerWon):
        if playerWon == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1
    
    def score(self):
        if (self.p1points==self.p2points):
            result = self.equalgame(self.p1points)
        elif self.p1points >= 4 or self.p2points >= 4:
            result = self.fourplusgame( self.p1points, self.p2points)
        else:
            result = self.othercase(self.p1points)
        return result
    
    def fourplusgame(self, point1, point2):
            result = point1 - point2
            if result == 1:
                result ="Advantage " + self.player1Name
            elif result == -1:
                result ="Advantage " + self.player2Name
            elif result >= 2:
                result = "Win for " + self.player1Name
            else:
                result = "Win for " + self.player2Name
            return result

    def othercase(self, point1, point2):
        for i in range(1,3):
                if (i==1):
                    self.tempScore = point1
                else:
                    result+="-"
                    self.tempScore = point2
                result += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[self.tempScore]
        return result
    
    def equalgame(self, point1):
            result = {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.p1points, "Deuce")
            return result