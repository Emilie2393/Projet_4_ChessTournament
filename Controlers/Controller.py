from Models.Player import Player
from Models.Match import Match
from Models.Tour import Tour
from typing import List
import random


class Controller:

    def __init__(self, view):
        self.players: List[Player] = []
        self.view = view
        self.scores = {}

    def get_players(self):
        """Get some players."""
        while len(self.players) < 8:
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name[0], name[1], name[2])
            self.players.append(player)
        print(self.players)

    def init_scores(self):
        for i in self.players:
            self.scores[i] = 0
        print(self.scores)

    def start_matches(self, round):
        rank = len(self.players)
        r = round
        tour = Tour("Round" + str(r))
        for i in range(0, rank, 2):
            scores = self.view.get_score(self.players[i], self.players[i + 1])
            score_1 = scores[0]
            score_2 = scores[1]
            print(type(score_2))
            player_1 = self.players[i]
            player_2 = self.players[i + 1]
            print(player_1, player_2)
            match = Match(player_1, score_1, player_2, score_2)
            tour.add_match(match)
            self.scores[player_1] += score_1
            self.scores[player_2] += score_2
            print("score", self.scores, "players", self.players)
        wait = self.view.next_tour()

    def sort_players(self):
        sorted_dic = dict(sorted(self.scores.items(), key=lambda item: item[1], reverse=True))
        print("player", self.players, "score", sorted_dic)
        self.players = list(sorted_dic.keys())
        return self.players

    def run(self):
        """Run the game."""
        self.get_players()
        self.init_scores()
        for i in range(4):
            self.start_matches(i)
            self.sort_players()
        """self.sort_players()"""
