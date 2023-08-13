
class Match:

    def __init__(self, player_1, score_1, player_2, score_2):
        self.player_1 = [player_1, score_1]
        self.player_2 = [player_2, score_2]
        self.match = (self.player_1, self.player_2)

    def __str__(self):
        return f"{self.match}"

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        return self.match[key]
