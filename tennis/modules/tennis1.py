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

    def winner(self):
        if ((self.p1points>=4 or self.p2points>=4) and self.p1points-self.p2points == 1):
            result =["A" , self.player1Name]
        elif ((self.p1points>=4 or self.p2points>=4) and self.p1points-self.p2points == -1):
            result =["A" , self.player2Name]
        elif ((self.p1points>=4 or self.p2points>=4) and self.p1points-self.p2points >=2):
            result = ["W" , self.player1Name]
        elif (self.p1points>=4 or self.p2points>=4):
            result =["W" , self.player2Name]
        else:
            result = ["N", '']
        return result

    
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
        else :
            victory=self.winner()
            match victory[0]:
                case 'A':
                    result = "Advantage " + victory[1]
                case 'W':
                    result = "Win for " + victory[1]
                case 'N':
                    result = result_list.get(self.p1points) +'-' + result_list.get(self.p2points)
        return result