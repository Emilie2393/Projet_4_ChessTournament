from Controlers.tournament_controller import TournamentController
from typing import List
import random


class MainController:

    def __init__(self, view, tournament):
        self.view = view
        self.tournament = tournament

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
                self.tournament.get_players()
                self.first_menu()
            if datas == "2":
                print("en construction")
                self.first_menu()

    def tournament_menu(self):
        datas = 0
        while datas != "1" or "2":
            datas = self.view.tournament_menu()
            if datas == "1":
                self.tournament.get_tournament()
                self.first_menu()
            if datas == "2":
                print("en construction")
                self.first_menu()

