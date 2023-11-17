class TennisGame:
    scoremax =4
    deuceValue=6
    def __init__(self, player1Name, player2Name):
        self.p1Name = player1Name
        self.p2Name = player2Name
        self.p1Score = 0
        self.p2Score = 0

    def won_point(self, n):
        if n == self.p1Name:
            self.p1Score += 1
        else:
            self.p2Score += 1

    def score(self):
        if (self.p1Score < self.scoremax and self.p2Score < self.scoremax) and (self.p1Score + self.p2Score < self.deuceValue):
            p = ["Love", "Fifteen", "Thirty", "Forty"]

            return p[self.p1Score] + "-All" if (self.p1Score == self.p2Score) else p[self.p1Score] + "-" + p[self.p2Score]
        else:
            if (self.p1Score == self.p2Score):
                return "Deuce"
            scoreLeader = self.p1Name if self.p1Score > self.p2Score else self.p2Name
            return "Advantage " + scoreLeader if ((self.p1Score-self.p2Score)*(self.p1Score-self.p2Score) == 1) else "Win for " + scoreLeader