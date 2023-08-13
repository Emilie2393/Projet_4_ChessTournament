
class MainController:

    def __init__(self, view, tournament, players, data, reports):
        self.view = view
        self.tournament = tournament
        self.players = players
        self.data = data
        self.reports = reports

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

    def players_menu(self):
        choice = 0
        while choice != "1" or "2" or "3" or "4" or "5":
            choice = self.view.players_menu()
            # create new players
            if choice == "1":
                self.players.create_player()
            # get all players
            if choice == "2":
                self.players.see_players()
            # create tournament players list
            if choice == "3":
                self.players.init_tournament_players()
            # get tournament players list
            if choice == "4":
                self.players.see_tournament_players()
            # delete tournament players list
            if choice == "5":
                self.players.del_tournament_players()
            if choice == "6":
                self.first_menu()

    def tournament_menu(self):
        choice = 0
        while choice != "1" or "2" or "3" or "4":
            choice = self.view.tournament_menu()
            # tournament creation
            if choice == "1":
                self.tournament.create_tournament()
            # tournament selection
            if choice == "2":
                if self.tournament.select_tournament():
                    self.players_menu()
            # delete all tournaments
            if choice == "3":
                self.tournament.del_tournament()
            # back to first menu
            if choice == "4":
                self.first_menu()

    def data_menu(self):
        choice = 0
        while choice != "1" or "2" or "3":
            choice = self.view.data_menu()
            if choice == "1":
                # see players
                self.reports.data_players()
            if choice == "2":
                # see tournament details
                self.reports.data_tournament()
            if choice == "3":
                self.first_menu()
                break
