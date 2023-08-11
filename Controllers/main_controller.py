from datetime import datetime


class MainController:

    def __init__(self, view, tournament, players, data):
        self.view = view
        self.tournament = tournament
        self.players = players
        self.data = data

    def first_menu(self):
        choice = 0
        while choice != "1" or "2" or "3":
            choice = self.view.main_menu()
            if choice == "1":
                self.players_menu()
            if choice == "2":
                self.tournament_menu()
            if choice == "3":
                self.data_menu()

    def create_player(self):
        status = 0
        # register players in json
        while status != "stop":
            self.players.get_new_players()
            self.data.players_desencoder("all_players")
            status = self.tournament.stop_tournament("à enregistrer des joueurs ?")

    def see_players(self):
        if not self.data.players:
            print("la liste est vide, merci de créer des joueurs")
            self.players_menu()
        else:
            to_print = self.data.players_desencoder("all_players")
            for player in to_print:
                print(player[0], player[1])
            self.players_menu()

    def associate_players(self):
        while len(self.data.tournament_players) < 8:
            for i in range(len(self.data.players.all())):
                print(i + 1, self.data.players.all()[i])
            players_choice = self.view.choose_players()
            name = self.players.tournament_players(players_choice)
            if name in self.data.tournament_players.all():
                print("Ce joueur est déjà dans la liste des joueurs du tournoi")
            else:
                self.data.save_tournament_player(name)
        self.tournament.players = self.data.players_desencoder("tournament_players")

    def init_tournament_players(self):
        if not self.data.players:
            print("la liste est vide, merci de créer des joueurs")
            self.players_menu()
        if len(self.data.players) < 8:
            print("il y a actuellement", len(self.data.players), "joueurs enregistrés")
            print("il n'y a pas assez de joueurs, merci de créer des joueurs supplémentaires")
            self.players_menu()
        if len(self.data.tournament_players) < 8:
            self.associate_players()
        status = self.tournament.stop_tournament("vers le menu tournoi")
        if status == "stop":
            self.players_menu()
        else:
            self.tournament_menu()

    def see_tournament_players(self):
        if not self.data.tournament_players:
            print("il n'y a pas de liste enregistrée")
        else:
            print(self.data.players_desencoder("tournament_players"))

    def del_tournament_players(self):
        self.data.delete_tournament_player()

    def create_tournament(self):
        self.tournament.get_tournament()
        to_save = self.data.tournament_encoder(self.tournament.tournament)
        self.data.save_tournament(to_save)
        if not self.data.tournament_players:
            print("Il n'y a pas de joueurs pour ce tournoi, merci d'en selectionner")
            self.players_menu()
        else:
            print("Votre tournoi est créé et prêt à être selectionné")

    def select_tournament(self):
        if not self.data.tournament:
            print("pas de tournoi enregistré, merci d'en créer un nouveau")
            self.tournament_menu()
        else:
            for i in range(len(self.data.tournament.all())):
                print(i + 1, self.data.tournament.all()[i])
            status = self.tournament.stop_tournament("le choix du tournoi")
            if status == "stop":
                self.tournament_menu()
            else:
                tournament_choice = self.view.choose_tournament()
                self.tournament.tournament_choice(tournament_choice)
                print("Tournoi sélectionné : ", self.tournament.tournament)
                print("data", self.data.get_tournament(tournament_choice))
                if not self.tournament.tournament.players_list:
                    if self.data.tournament_players:
                        self.tournament.tournament.players_list = self.data.players_desencoder("tournament_players")
                        print(self.data.players_desencoder("tournament_players"))
                        status = self.tournament.stop_tournament("avec ces joueurs")
                        if status == "stop":
                            self.first_menu()
                        if status == "players_menu":
                            self.tournament.tournament.players_list = []
                            self.data.delete_tournament_player()
                            self.players_menu()
                        # tournament start
                        else:
                            self.data.update_tournament_data(self.tournament.tournament.name,
                                                             self.tournament.tournament.players_list,
                                                             datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                            self.tournament.players = self.tournament.tournament.players_list
                            self.tournament.new_tournament()
                    else:
                        print("merci de selectionner les joueurs de ce tournoi")
                        self.players_menu()
                else:
                    self.tournament.players = self.tournament.tournament.players_list
                    status = self.tournament.stop_tournament("le tournoi")
                    if status == "stop":
                        self.tournament_menu()
                    else:
                        self.data.update_tournament_data(self.tournament.tournament.name,
                                                         self.tournament.tournament.players_list,
                                                         datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                        self.tournament.new_tournament()

    def del_tournament(self):
        if not self.data.tournament:
            print("pas de tournoi enregistré, merci d'en créer un nouveau")
            self.tournament_menu()
        else:
            self.data.delete_tournaments()
            print("Tournois supprimés")
            self.tournament_menu()

    def players_menu(self):
        choice = 0
        while choice != "1" or "2" or "3" or "4" or "5":
            choice = self.view.players_menu()
            # create new players
            if choice == "1":
                self.create_player()
                break
            # get all players
            if choice == "2":
                self.see_players()
            # create tournament players list
            if choice == "3":
                self.init_tournament_players()
            # get tournament players list
            if choice == "4":
                self.see_tournament_players()
            # delete tournament players list
            if choice == "5":
                self.del_tournament_players()
            if choice == "6":
                self.first_menu()

    def tournament_menu(self):
        choice = 0
        while choice != "1" or "2" or "3" or "4":
            choice = self.view.tournament_menu()
            # tournament creation
            if choice == "1":
                self.create_tournament()
            # tournament selection
            if choice == "2":
                self.select_tournament()
            # delete all tournaments
            if choice == "3":
                self.del_tournament()
            # back to first menu
            if choice == "4":
                self.first_menu()

    def data_menu(self):
        choice = 0
        while choice != "1" or "2" or "3":
            choice = self.view.data_menu()
            if choice == "1":
                self.view.data_players()
                self.data_menu()
            if choice == "2":
                data = self.view.data_tournament()
                if not data:
                    self.data_menu()
            if choice == "3":
                self.first_menu()
                break
