from Models.Player import Player
from Models.Match import Match
from Models.Tour import Tour
from Models.Tournament import Tournament
from typing import List
import random


class TournamentController:

    def __init__(self, view):
        self.tournament = []
        self.players: List[Player] = []
        self.previous_players_list = []
        self.view = view
        self.scores = {}

    def get_tournament(self):
        datas = self.view.prompt_for_tournament()
        name = datas[0]
        place = datas[1]
        start_date = datas[2]
        end_date = datas[3]
        rounds_nb = datas[4]
        tournament = Tournament(name, place, start_date, end_date, rounds_nb)
        self.tournament = tournament
        print(self.tournament)

    def get_players(self):
        """Get some players."""
        while len(self.players) < 8:
            name = self.view.prompt_for_player()
            if not name:
                return
            player = Player(name)
            self.players.append(player)

    def init_scores(self):
        for i in self.players:
            self.scores[i] = 0
        print(self.scores)

    def start_matches(self, round):
        rank = len(self.players)
        r = round
        tour = Tour("Round" + str(r))
        tour.matches = []
        for i in range(0, rank, 2):
            scores = self.view.get_score(self.players[i], self.players[i + 1])
            match = Match(self.players[i], scores[0], self.players[i + 1], scores[1])
            tour.add_match(match)
            self.scores[self.players[i]] += scores[0]
            self.scores[self.players[i + 1]] += scores[1]
            print("score", self.scores, "players", self.players)
            print("tour matchs : ", tour.matches)
        tournament = self.tournament
        tournament.add_tour(tour)
        for i in self.players:
            self.previous_players_list.append(i)
        print("tours list", self.tournament.tours_list)
        wait = self.view.next_tour()

    def check_identical_matches(self, sorted_keys, start_list=0):
        len_sort_keys = len(sorted_keys)
        len_prev_matches = len(self.previous_players_list)
        for i in range(start_list, len_prev_matches, 2):
            old_match = self.previous_players_list[i], self.previous_players_list[i + 1]
            print("i", old_match)
            for e in range(0, len_sort_keys, 2):
                new_match = sorted_keys[e], sorted_keys[e + 1]
                print("avant", sorted_keys)
                if new_match == old_match and e < (len_sort_keys - 2):
                    sorted_keys[e], sorted_keys[e + 2] = sorted_keys[e + 2], sorted_keys[e]
                    print("apres", sorted_keys)
                    self.check_identical_matches(sorted_keys, start_list=i)
                if new_match == old_match and e > (len_sort_keys - 2):
                    sorted_keys[e], sorted_keys[e - 2] = sorted_keys[e - 2], sorted_keys[e]
                    print("apres", sorted_keys)
                print("e", new_match)
        self.players = sorted_keys
        print(self.players)

    def sort_players(self):
        sorted_scores = dict(sorted(self.scores.items(), key=lambda item: item[1], reverse=True))
        sorted_keys = list(sorted_scores.keys())
        print("player", self.players, "score", sorted_scores)
        self.check_identical_matches(sorted_keys)

    def run(self):
        """Run the game."""
        self.get_tournament()
        self.get_players()
        self.init_scores()
        for i in range(1, 5):
            self.start_matches(i)
            if i < 4:
                self.sort_players()
        """self.sort_players()"""
