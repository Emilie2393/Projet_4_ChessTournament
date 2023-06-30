from Controlers.tournament_controller import TournamentController
from Models.Datas import Data
from typing import List
import random


class MainController:

    def __init__(self, view, tournament, players):
        self.view = view
        self.tournament = tournament
        self.players = players

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
        while datas != "1" or "2":
            datas = self.view.players_menu()
            if datas == "1":
                status = 0
                while status != "stop":
                    self.players.get_new_players()
                    status = self.tournament.stop_tournament("les joueurs")
                break
            if datas == "2":
                data = Data()
                for i in range(len(data.players.all())):
                    print(i+1, data.players.all()[i])
                while len(self.players.players_list) < 8:
                    choices = self.view.choose_players()
                    self.players.tournament_players(choices)
                status = self.tournament.stop_tournament("les joueurs")
                if status == "stop":
                    data.save_tournament_player(self.players.players_list)
                else:
                    self.tournament.players_list = self.players.players_list
                    print(self.tournament.players_list)
                    self.tournament_menu()




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
