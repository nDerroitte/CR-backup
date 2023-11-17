class TennisGameGPT:
    SCORE_MAPPING = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

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
        if self.p1points == self.p2points:
            return self._handle_tie_score()
        elif self.p1points >= 4 or self.p2points >= 4:
            return self._handle_advantage_or_win()
        else:
            return self._handle_regular_score()

    def _handle_tie_score(self):
        return {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.p1points, "Deuce")

    def _handle_advantage_or_win(self):
        minus_result = self.p1points - self.p2points
        if minus_result == 1:
            return "Advantage " + self.player1Name
        elif minus_result == -1:
            return "Advantage " + self.player2Name
        elif minus_result >= 2:
            return "Win for " + self.player1Name
        else:
            return "Win for " + self.player2Name

    def _handle_regular_score(self):
        result = ""
        for i, player_points in enumerate([self.p1points, self.p2points]):
            if i == 1:
                result += "-"
            result += self.SCORE_MAPPING[player_points]
        return result
