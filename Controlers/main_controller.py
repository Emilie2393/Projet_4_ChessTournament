from Controlers.tournament_controller import TournamentController
from Models.Datas import Data
from typing import List
import random


class MainController:

    def __init__(self, view, tournament, players, data):
        self.view = view
        self.tournament = tournament
        self.players = players
        self.data = data

    def first_menu(self):
        datas = 0
        while datas != "1" or "2":
            datas = self.view.main_menu()
            if datas == "1":
                self.players_menu()
            if datas == "2":
                self.tournament_menu()

    def players_menu(self):
        datas = 0
        tournament_players_list = self.players.players_list
        json_players = self.data.players
        json_tournament_players = self.data.tournament_players
        while datas != "1" or "2" or "3" or "4" or "5":
            datas = self.view.players_menu()
            if datas == "1":
                status = 0
                # register players in json
                while status != "stop":
                    self.players.get_new_players()
                    self.data.players_desencoder("all_players")
                    status = self.tournament.stop_tournament("enregistrer un nouveau joueur ?")
                break
            if datas == "2":
                if not json_players:
                    print("la liste est vide, merci de créer des joueurs")
                    self.players_menu()
                    break
                else:
                    self.data.players_desencoder("all_players")
            if datas == "3":
                if not json_players:
                    print("la liste est vide, merci de créer des joueurs")
                    self.players_menu()
                    break
                if len(json_players) < 8:
                    self.data.players_desencoder("players")
                    print("il n'y a pas assez de joueurs, merci de créer des joueurs supplémentaires")
                    self.players_menu()
                    break
                for i in range(len(json_players.all())):
                    print(i + 1, json_players.all()[i])
                while len(tournament_players_list) < 8:
                    choices = self.view.choose_players()
                    self.players.tournament_players(choices)
                status = self.tournament.stop_tournament(" ")
                if status == "stop":
                    self.data.save_tournament_player(tournament_players_list)
                    self.tournament.players = tournament_players_list
                    print(self.tournament.players)
                    break
                else:
                    self.data.save_tournament_player(tournament_players_list)
                    self.tournament.players = tournament_players_list
                    print(self.tournament.players)
                    self.tournament_menu()
                    break
            if datas == "4":
                to_check = self.data.check_tournament_player()
                if not to_check:
                    print("il n'y a pas de liste enregistrée")
                else:
                    self.data.players_desencoder("tournament_players")

            if datas == "5":
                to_delete = self.data.delete_tournament_player()
                print(to_delete)
                if not to_delete:
                    print("il n'y a pas de liste enregistrée")
                else:
                    print(json_tournament_players)
            if datas == "6":
                self.first_menu()

    def tournament_menu(self):
        datas = 0
        while datas != "1" or "2":
            datas = self.view.tournament_menu()
            if datas == "1":
                self.tournament.get_tournament()
                self.players_menu()
                self.tournament.new_tournament()
            if datas == "2":
                print("en construction")
                self.first_menu()
