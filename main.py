import random


class Player:
    players_list = []

    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return str(self)

    def add_player(self, new):
        for i in new:
            self.players_list.append(i)
        return self.players_list


class Match:

    def __init__(self, player_1, score_1, player_2, score_2):
        self.player_1 = [player_1, score_1]
        self.player_2 = [player_2, score_2]
        self.match = (self.player_1, self.player_2)

    def __str__(self):
        return f"{self.match}"

    def __repr__(self):
        return str(self)


class Tour:
    match_list = []

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)

    def add_match(self, new):
        for i in new:
            self.match_list.append(i)
        return self.match_list


new_player = Player("Jacques", "Richard", "05/06/90")
new_player2 = Player("Michel", "Rdhue", "05/08/95")
new_player3 = Player("René", "chinon", "25/01/78")
new_player.add_player([new_player, new_player2, new_player3])
print(Player.players_list)
match_one = Match(new_player, 2, new_player2, 1)
match_two = Match(new_player3, 1, new_player, 0)
print(match_one.match)
round1 = Tour("Round 1")
test = round1.add_match([match_one, match_two])
print(test)
