from Models.Player import Player
from Models.Match import Match
from Models.Tour import Tour
from typing import List


class Controller:

    def __init__(self, view):
        self.players: List[Player] = []
        self.view = view

    def get_players(self):
        """Get some players."""
        while len(self.players) < 8:
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name[0], name[1], name[2])
            self.players.append(player)
        print(self.players)

    def start_matches(self):
        rank = len(self.players)
        r = 1
        tour = Tour("Round" + str(r))
        for i in range(0, rank, 2):
            scores = self.view.get_score()
            score_1 = scores[0]
            score_2 = scores[1]
            player_1 = self.players[i]
            player_2 = self.players[i+1]
            match = Match(player_1, score_1, player_2, score_2)
            tour.add_match(match)
            print(match)
        print(tour)

    def run(self):
        """Run the game."""
        self.get_players()
        self.start_matches()
