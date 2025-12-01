
class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3

    SCORE_NAMES = {
        LOVE: "Love",
        FIFTEEN: "Fifteen",
        THIRTY: "Thirty",
        FORTY: "Forty"
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.is_tie():
            return self.tie_score()
        if self.is_endgame():
            return self.endgame_score()
        return self.normal_score()

    def is_tie(self):
        return self.player1_score == self.player2_score

    def is_endgame(self):
        return self.player1_score >= 4 or self.player2_score >= 4

    def tie_score(self):
        if self.player1_score < 3:
            return f"{self.SCORE_NAMES[self.player1_score]}-All"
        return "Deuce"

    def endgame_score(self):
        score_diff = self.player1_score - self.player2_score
        if score_diff == 1:
            return f"Advantage {self.player1_name}"
        elif score_diff == -1:
            return f"Advantage {self.player2_name}"
        elif score_diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def normal_score(self):
        return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"
