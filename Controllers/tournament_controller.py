import random
from Models.player import Player
from Models.match import Match
from Models.tour import Tour
from Models.tournament import Tournament
from Models.data import Data
from typing import List
from datetime import datetime


class TournamentController:

    def __init__(self, view, data):
        self.data = data
        self.view = view
        self.tournament = []
        self.players: List[Player] = []

    def create_tournament(self):
        self.get_tournament()
        self.data.tournament_serialize(self.tournament)
        if not self.data.tournament_players:
            print("Il n'y a pas de joueurs pour ce tournoi, merci d'en selectionner")
        else:
            print("Votre tournoi est créé et prêt à être selectionné")

    def select_tournament(self):
        if not self.data.tournament:
            print("pas de tournoi enregistré, merci d'en créer un nouveau")
        else:
            for i in range(len(self.data.tournament.all())):
                print(i + 1, self.data.tournament.all()[i])
            status = self.stop_tournament("le choix du tournoi")
            if status == "stop":
                return
            else:
                tournament_choice = self.view.choose_tournament()
                self.tournament_choice(tournament_choice)
                print("Tournoi sélectionné : ", self.tournament)
                print("data", self.data.get_tournament(tournament_choice))
                if not self.tournament.players_list:
                    if self.data.tournament_players:
                        self.tournament.players_list = self.data.players_deserialize("tournament_players")
                        print(self.data.players_deserialize("tournament_players"))
                        status = self.stop_tournament("avec ces joueurs")
                        if status == "stop":
                            return
                        if status == "players_menu":
                            self.tournament.players_list = []
                            self.data.delete_tournament_player()
                            return True
                        # tournament start
                        else:
                            self.data.update_tournament_data(self.tournament.name, self.tournament.players_list,
                                                             datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                            self.players = self.tournament.players_list
                            self.new_tournament()
                    else:
                        print("merci de selectionner les joueurs de ce tournoi")
                        return True
                else:
                    status = self.stop_tournament("le tournoi")
                    if status == "stop":
                        return
                    else:
                        self.data.update_tournament_data(self.tournament.name, self.tournament.players_list,
                                                         datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                        self.players = self.tournament.players_list
                        self.new_tournament()

    def del_tournament(self):
        if not self.data.tournament:
            print("pas de tournoi enregistré, merci d'en créer un nouveau")
        else:
            self.data.delete_tournaments()
            print("Tournois supprimés")

    def tournament_choice(self, selected):
        selection = self.data.get_tournament(selected)
        selected = self.data.tournament_deserialize(selection)
        tournament = Tournament(selected[0], selected[1], selected[2], selected[3], selected[4], selected[5],
                                selected[6], selected[7], selected[8], selected[9])
        self.tournament = tournament

    def get_tournament(self):
        data = self.view.prompt_for_tournament()
        name = data[0]
        place = data[1]
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
            self.data.scores[i] = 0
        print(self.data.scores)

    def check_previous_data(self, tournament, matches, tour, tour_progress):
        if tournament.round == 1 and not tournament.tours_list:
            random.shuffle(self.players)
            self.data.update_tournament_data(tournament.name, self.players)
        if tournament.tours_list:
            # if round is over, next round
            if len(tournament.tours_list[len(tournament.tours_list) - 1]
                   ["Round" + str(len(tournament.tours_list))]) > 3:
                tour_progress = 0
                self.data.tours_to_save = tournament.tours_list
                self.sort_players()
            # if round has already begun
            else:
                for match in matches:
                    keys = list(match.keys())
                    values = list(match.values())
                    deserialize = Match(keys[0], values[0], keys[1], values[1])
                    tour.add_match(deserialize)
                for e in range(len(tournament.tours_list) - 1):
                    self.data.tours_to_save.append(tournament.tours_list[e])
        return tour_progress

    def start_matches(self, tour_nb, tour_progress, matches):
        tournament = self.tournament
        rank = len(self.players)
        tour = Tour("Round" + str(tour_nb))
        tour.matches = []
        self.data.tours_to_save = []
        self.data.prev_games = tournament.prev_games
        # init tour progress if round has already begun
        tour_progress = self.check_previous_data(tournament, matches, tour, tour_progress)
        # one round
        for i in range(tour_progress, rank, 2):
            player1 = self.players[i]
            player2 = self.players[i + 1]
            scores = self.view.get_score(player1, player2)
            match = Match(player1, scores[0], player2, scores[1])
            tour.add_match(match)
            self.data.scores[player1] += scores[0]
            self.data.scores[player2] += scores[1]
            status = self.stop_tournament("tour")
            if status == "stop":
                break
            else:
                continue
        self.data.tours_list_serialize(tour, tournament.name)
        if len(tour.matches) > 3:
            tournament.round += 1
        for i in self.players:
            self.data.prev_games.append(i)
        self.data.update_tournament_tours(tournament.name, self.data.scores, self.data.prev_games, tournament.round)
        new = self.data.tournament_deserialize(self.data.check_tournament(tournament.name)[0])
        self.tournament = Tournament(new[0], new[1], new[2], new[3], new[4], new[5],
                                     new[6], new[7], new[8])
        status = self.stop_tournament("le tournoi en cours ou l'enregistrer")
        if status == "stop":
            return False
        else:
            return True

    def check_identical_matches(self, sorted_keys, start_list=0):
        len_sort_keys = len(sorted_keys)
        len_prev_matches = int(len(self.data.prev_games) / 2)
        for i in range(start_list, len_prev_matches, 2):
            old_match = self.data.prev_games[i], self.data.prev_games[i + 1]
            print("i", i, len_prev_matches, old_match)
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
        print("fin", sorted_keys)
        self.players = sorted_keys

    def sort_players(self):
        sorted_scores = dict(sorted(self.data.scores.items(), key=lambda item: item[1], reverse=True))
        sorted_keys = list(sorted_scores.keys())
        self.check_identical_matches(sorted_keys)

    def new_tournament(self):
        self.init_scores()
        start = 1
        end = True
        tours = self.tournament.tours_list
        games = []
        in_process = 0
        if tours:
            start = start + len(tours)
            self.data.scores = self.tournament.scores
            print(tours)
            if len(tours[len(tours) - 1]["Round" + str(len(tours))]) < 4:
                in_process = 2 * len(tours[len(tours) - 1]["Round" + str(len(tours))])
                games = tours[len(tours) - 1]["Round" + str(len(tours))]
                start = len(tours)
        for tour in range(start, 5):
            print("tour", tour, "inprocess", in_process, "games", games)
            tournament = self.start_matches(tour, in_process, games)
            if not tournament:
                self.data.update_tournament_data(self.tournament.name, self.players)
                end = False
                break
        if end:
            self.tournament.end_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            self.data.update_tournament_data(self.tournament.name, [], 0, self.tournament.end_date)
            sorted_scores = dict(sorted(self.data.scores.items(), key=lambda item: item[1],
                                        reverse=True))
            print(f"Le tournoi {self.tournament.name} est terminé ! \nVoici les scores : {sorted_scores}")
