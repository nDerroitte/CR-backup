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
    
    def score(self):
        result = ""
        tempScore=0
        result_list= {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty"
                }
        if (self.p1points==self.p2points ):
            result = (result_list.get(self.p1points, "Deuce")).replace("Forty","Deuce")
            if result != "Deuce":
                result = result +"-All"
        elif ((self.p1points>=4 or self.p2points>=4) and self.p1points-self.p2points == 1):
            result ="Advantage " + self.player1Name
        elif ((self.p1points>=4 or self.p2points>=4) and self.p1points-self.p2points == -1):
            result ="Advantage " + self.player2Name
        elif ((self.p1points>=4 or self.p2points>=4) and self.p1points-self.p2points >=2):
            result = "Win for " + self.player1Name
        elif (self.p1points>=4 or self.p2points>=4):
            result ="Win for " + self.player2Name
        else:
            tempScore = [self.p1points, self.p2points]
            result1 = [result_list[i] for i in tempScore ]
            result = '-'.join(map(str, result1))
        return result