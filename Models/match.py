#from Player import new_player, new_player2, new_player3


class Match:

    def __init__(self, player_1, score_1, player_2, score_2):
        self.player_1 = [player_1, score_1]
        self.player_2 = [player_2, score_2]
        self.match = (self.player_1, self.player_2)

    def __str__(self):
        return f"{self.match}"

    def __repr__(self):
        return str(self)


"""match_one = Match(new_player, 2, new_player2, 1)
match_two = Match(new_player3, 1, new_player, 0)
print("Match(Player(...), 2) : ", match_one.match)"""
