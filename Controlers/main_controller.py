from Controlers.tournament_controller import TournamentController
from Models.Datas import Data


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
                if self.tournament.tournament:
                    if json_tournament_players:
                        print("ce tournoi est selectionné : ")
                        print(self.tournament.tournament)
                        print("souhaitez-vous lui affilier ces joueurs ? :")
                        self.data.players_desencoder("tournament_players")
                        status = self.tournament.stop_tournament("cette association")
                        if status == "stop":
                            self.data.delete_tournament_player()
                            self.players_menu()
                            break
                        else:
                            self.data.update_tournament(self.tournament.tournament['name'], tournament_players_list)
                    else:
                        if len(tournament_players_list) < 8:
                            for i in range(len(json_players.all())):
                                print(i + 1, json_players.all()[i])
                            while len(tournament_players_list) < 8:
                                players_choice = self.view.choose_players()
                                self.players.tournament_players(players_choice)
                                self.data.save_tournament_player(tournament_players_list)
                                self.tournament.players = tournament_players_list
                        print(f"cette liste va être enregistrée dans le tournoi {self.tournament.tournament['name']}")
                        self.data.players_desencoder("tournament_players")
                        status = self.tournament.stop_tournament("vers le tournoi")
                        self.data.save_tournament_player(tournament_players_list)
                        self.tournament.players = tournament_players_list
                        if status == "stop":
                            self.players_menu()
                            break
                        else:
                            self.tournament_menu()
                            break
                else:
                    if len(tournament_players_list) < 8:
                        for i in range(len(json_players.all())):
                            print(i + 1, json_players.all()[i])
                        while len(tournament_players_list) < 8:
                            players_choice = self.view.choose_players()
                            self.players.tournament_players(players_choice)
                    status = self.tournament.stop_tournament("vers le tournoi")
                    self.data.save_tournament_player(tournament_players_list)
                    self.tournament.players = tournament_players_list
                    if status == "stop":
                        self.players_menu()
                        break
                    else:
                        self.tournament_menu()
                        break

            if datas == "4":
                to_check = self.data.check_tournament_player()
                if not to_check:
                    print("il n'y a pas de liste enregistrée")
                else:
                    if self.tournament.tournament:
                        if not json_tournament_players:
                            print("ce tournoi est selectionné : ")
                            print(self.tournament.tournament)
                            print("souhaitez-vous lui affilier ces joueurs ? :")
                            self.data.players_desencoder("tournament_players")
                            status = self.tournament.stop_tournament("cette association")
                            if status == "stop":
                                self.data.delete_tournament_player()
                                self.players_menu()
                                break
                            else:
                                self.data.update_tournament(self.tournament.tournament['name'],
                                                            self.data.players_desencoder("tournament_players"))
                        else:
                            if self.tournament.tournament['players_list']:
                                self.data.players_desencoder("tournament_players")
                            else:
                                self.data.players_desencoder("tournament_players")
                                status = self.tournament.stop_tournament("cette association")
                                if status == "stop":
                                    self.data.delete_tournament_player()
                                    self.players_menu()
                                    break
                                else:
                                    self.data.update_tournament(self.tournament.tournament['name'],
                                                                self.data.players_desencoder("tournament_players"))
                    else:
                        self.data.players_desencoder("tournament_players")

            if datas == "5":
                to_delete = self.data.delete_tournament_player()
                print(to_delete)
                if not to_delete:
                    print("il n'y a pas de liste enregistrée")
                else:
                    self.data.players_desencoder("tournament_players")
            if datas == "6":
                self.first_menu()

    def tournament_menu(self):
        datas = 0
        tournament = self.tournament
        json_tournament = self.data.tournament
        json_tournament_players = self.data.tournament_players
        while datas != "1" or "2":
            datas = self.view.tournament_menu()
            if datas == "1":
                tournament.get_tournament()
                to_save = self.data.tournament_encoder(tournament.tournament)
                self.data.save_tournament(to_save)
                if not json_tournament_players:
                    print("il n'y a pas de joueurs pour ce tournoi, merci d'en selectionner")
                    self.players_menu()
                    break
                tournament.tournament.players_list = self.data.players_desencoder("tournament_players")
                status = tournament.stop_tournament("avec ces joueurs")
                if status == "stop":
                    self.first_menu()
                    break
                if status == "players_menu":
                    tournament.tournament.players_list = []
                    self.players_menu()
                else:
                    to_save = self.data.tournament_encoder(tournament.tournament)
                    self.data.save_tournament(to_save)
                    tournament.players = tournament.tournament.players_list
                    tournament.new_tournament()
                    break
            if datas == "2":
                if not json_tournament:
                    print("pas de tournoi enregistré, merci d'en créer un nouveau")
                    self.tournament_menu()
                    break
                else:
                    for i in range(len(json_tournament.all())):
                        print(i + 1, json_tournament.all()[i])
                    status = self.tournament.stop_tournament("le choix du tournoi")
                    if status == "stop":
                        break
                    else:
                        tournament_choice = self.view.choose_tournament()
                        self.tournament.tournament_choice(tournament_choice)
                        if not tournament.tournament['players_list']:
                            print("merci de selectionner les joueurs de ce tournoi")
                            self.players_menu()
                        else:
                            tournament.players = tournament.tournament["players_list"]
                            status = self.tournament.stop_tournament("le tournoi")
                            if status == "stop":
                                break
                            else:
                                print(tournament.players)
                                tournament.new_tournament()
                                break

            if datas == "3":
                if not json_tournament:
                    print("pas de tournoi enregistré, merci d'en créer un nouveau")
                    self.tournament_menu()
                    break
                else:
                    self.data.delete_tournaments()
                    self.first_menu()
                    break
