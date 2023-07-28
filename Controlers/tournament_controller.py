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
                                selected[6], selected[7], selected[8], selected[9])
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
        scores = []
        prev_games = []
        rounds_nb = 4
        tournament = Tournament(name, place, start_date, end_date, tours_list, round, players_list,
                                scores, prev_games, rounds_nb)

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
        print(self.players[0])
        for i in self.players:
            # name = self.players[i][0] + " " + self.players[i][1]
            self.scores[i] = 0
        print(self.scores)

    def start_matches(self, round, e, matches):
        data = Data()
        tournament = self.tournament
        rank = len(self.players)
        r = round
        tour = Tour("Round" + str(r))
        tour.matches = []
        tours_list = []
        print("avant verif tour", tours_list)
        print("prev", tournament.prev_games)
        print(data.tours_to_save)
        ## probleme ici le tour précédent ne s'enregistre pas
        if tournament.tours_list:
            print(tournament.tours_list[len(tournament.tours_list) - 1]["Round" + str(len(tournament.tours_list))])
            print(len(tournament.tours_list[len(tournament.tours_list) - 1]["Round" + str(len(tournament.tours_list))]))
            self.previous_players_list = tournament.prev_games
            if len(tournament.tours_list[len(tournament.tours_list) - 1]
                   ["Round" + str(len(tournament.tours_list))]) > 3:
                print("heyehfhz")
                e = 0
                data.tours_to_save = tournament.tours_list
                self.sort_players()
            else:
                if matches:
                    data.tours_to_save = []
                    for i in matches:
                        tours_list.append(i)
                        print(tours_list)
                    for f in range(len(tournament.tours_list) - 1):
                        print(tournament.tours_list[f])
                        data.tours_to_save.append(tournament.tours_list[f])
                        print(data.tours_to_save)
                else:
                    e = 0
                    self.sort_players()
                    data.tours_to_save = tournament.tours_list
                    print(data.tours_to_save)
        print("ne", tournament)
        print(tournament.round)
        print("what", self.players)
        for i in range(e, rank, 2):
            player1 = self.players[i]  # [0] + " " + self.players[i][1]
            player2 = self.players[i + 1]  # [0] + " " + self.players[i + 1][1]
            scores = self.view.get_score(player1, player2)
            match = Match(player1, scores[0], player2, scores[1])
            tours_list.append({player1: scores[0], player2: scores[1]})
            print("jsons", tours_list)
            print(match)
            tour.add_match(match)
            self.scores[player1] += scores[0]
            self.scores[player2] += scores[1]
            print("score", self.scores, "players", self.players)
            status = self.stop_tournament("tour")
            if status == "stop":
                break
            else:
                continue
        # self.tours_list.append(tour)
        if len(tours_list) > 3:
            tournament.round += 1
        for i in self.players:
            self.previous_players_list.append(i)
        print(self.previous_players_list)
        print("tournament", self.tournament)
        print("tours_list", tours_list)
        print("yo", tournament.tours_list)
        print("tosave", data.tours_to_save)
        status = self.stop_tournament("le tournoi en cours ou l'enregistrer")
        data.tours_list_encoder(tour.name, tours_list)
        data.tours_list_insert(data.tours_to_save, tournament.name)
        data.scores = self.scores
        data.prev_games = self.previous_players_list
        print("to register", data.prev_games)
        new = data.tournament_desencoder(data.check_tournament(tournament.name)[0])
        self.tournament = Tournament(new[0], new[1], new[2], new[3], new[4], new[5],
                                     new[6], new[7], new[8])
        print("self.tournament end", self.tournament)
        print(data.scores)
        data.update_tournament_tours(tournament.name, data.scores, data.prev_games, tournament.round)
        if status == "stop":
            print("yoooooooooo")
            print(data.tours_to_save)
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
        print(sorted_keys)
        self.players = sorted_keys
        """
        for f in range(len(sorted_keys)):
            data = Data()
            name = data.find_full_player(sorted_keys[f])[0]
            print("check", self.players)
            print(name)
            sorted_players.append([name["firstname"], name["lastname"], name["birthdate"]])
        self.players = sorted_players"""

    def sort_players(self):
        sorted_scores = dict(sorted(self.scores.items(), key=lambda item: item[1], reverse=True))
        sorted_keys = list(sorted_scores.keys())
        print(sorted_keys)
        print("player", self.players, "score", sorted_scores)
        self.check_identical_matches(sorted_keys)

    def new_tournament(self):
        data = Data()
        self.init_scores()
        j = 1
        tours = self.tournament.tours_list
        matchs = []
        e = 0
        if tours:
            print(tours)
            j = j + len(tours)
            self.scores = self.tournament.scores
            print(len(tours))
            if len(tours[len(tours) - 1]["Round" + str(len(tours))]) < 4:
                print(tours[len(tours) - 1]["Round" + str(len(tours))])
                e = 2 * len(tours[len(tours) - 1]["Round" + str(len(tours))])
                matchs = tours[len(tours) - 1]["Round" + str(len(tours))]
                j = len(tours)
        for i in range(j, 5):
            print("i", i, "j", j, "e", e)
            tournament = self.start_matches(i, e, matchs)
            if not tournament:
                data.update_tournament_start(self.tournament.name, self.players)
                break
            # if i < 4:
            # self.sort_players()
        self.tournament.end_date = datetime.now()
