from Models.player import Player
from Models.match import Match
from Models.tour import Tour
from Models.tournament import Tournament
from Models.data import Data
from typing import List
from datetime import datetime


class TournamentController:

    def __init__(self, view):
        self.tournament = []
        self.players: List[Player] = []
        self.tours_list = []
        self.previous_players_list = []
        self.view = view
        self.scores = {}

    def tournament_choice(self, selected):
        data = Data()
        selection = data.get_tournament(selected)
        selected = data.tournament_desencoder(selection)
        tournament = Tournament(selected[0], selected[1], selected[2], selected[3], selected[4], selected[5],
                                selected[6], selected[7])
        self.tournament = tournament

    def get_tournament(self):
        datas = self.view.prompt_for_tournament()
        name = datas[0]
        place = datas[1]
        start_date = []
        end_date = []
        round = 1
        tours_list = []
        players_list = []
        rounds_nb = 4
        tournament = Tournament(name, place, start_date, end_date, tours_list, round, players_list,
                                rounds_nb)

        self.tournament = tournament
        print("t", self.tournament.name)
        return tournament

    def stop_tournament(self, state):
        choice = 0
        while choice != "1" or "2":
            choice = self.view.continue_or_not(state)
            if choice == "1":
                break
            if choice == "2":
                return "stop"
            if choice == "3":
                return "players_menu"

    def init_scores(self):
        for i in self.players:
            self.scores[i] = 0
        print(self.scores)

    def start_matches(self, round):
        data = Data()
        rank = len(self.players)
        r = round
        tour = Tour("Round" + str(r))
        tour.matches = []
        json_tours = []
        tournament = self.tournament
        print("ne", tournament)
        print(tournament.rounds_nb)
        if tournament.tours_list:
            data.tours_to_save = tournament.tours_list
            print(tournament.tours_list)
            print(data.tours_to_save)
            print("json", json_tours)
        for i in range(0, rank, 2):
            scores = self.view.get_score(self.players[i], self.players[i + 1])
            match = Match(self.players[i], scores[0], self.players[i + 1], scores[1])
            json_tours.append({self.players[i]: scores[0], self.players[i + 1]: scores[1]})
            print("jsons", json_tours)
            print(match)
            tour.add_match(match)
            self.scores[self.players[i]] += scores[0]
            self.scores[self.players[i + 1]] += scores[1]
            print("score", self.scores, "players", self.players)
            print("tour matchs : ", tour.matches)
            self.stop_tournament("tour")
        self.tours_list.append(tour)
        tournament.round += 1
        for i in self.players:
            self.previous_players_list.append(i)
        print("tournament", self.tournament)
        print("tour", self.tours_list)
        status = self.stop_tournament("le tournoi en tour ou l'enregistrer")
        data.tours_list_encoder(tour.name, json_tours)
        data.tours_list_insert(data.tours_to_save, tournament.name)
        if status == "stop":
            return False
        else:
            return True

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

    def new_tournament(self):
        self.init_scores()
        j = 1
        if self.tournament.tours_list:
            j = 5 - len(self.tournament.tours_list)
        for i in range(j, 5):
            tournament = self.start_matches(i)
            if not tournament:
                break
            if i < 4:
                self.sort_players()
        self.tournament.end_date = datetime.now()


