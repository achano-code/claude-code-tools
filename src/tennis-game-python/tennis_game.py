class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
    
    def win_ball(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
    
    def get_score(self):
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self._get_deuce_score()
        else:
            return f"{self._translate_score(self.player1_score)}-{self._translate_score(self.player2_score)}"
    
    def _translate_score(self, score):
        score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return score_names.get(score, "Forty")
    
    def _get_deuce_score(self):
        score_difference = self.player1_score - self.player2_score
        
        if score_difference == 0:
            return "Deuce"
        elif score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"