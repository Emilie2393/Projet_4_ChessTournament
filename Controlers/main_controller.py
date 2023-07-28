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

    def players_menu(self):
        choice = 0
        data = self.data
        json_players = data.players
        json_tournament_players = data.tournament_players
        tournament = self.tournament

        def associate_players():
            for i in range(len(json_players.all())):
                print(i + 1, json_players.all()[i])
            while len(json_tournament_players) < 8:
                players_choice = self.view.choose_players()
                data.save_tournament_player(self.players.tournament_players(players_choice))
            tournament.players = data.players_desencoder("tournament_players")
            if tournament.tournament:
                tournament.tournament.players_list = data.players_desencoder("tournament_players")
                data.update_tournament_start(tournament.tournament.name, data.players_desencoder("tournament_players"))

        while choice != "1" or "2" or "3" or "4" or "5":
            choice = self.view.players_menu()
            # create new players
            if choice == "1":
                status = 0
                # register players in json
                while status != "stop":
                    self.players.get_new_players()
                    data.players_desencoder("all_players")
                    status = tournament.stop_tournament("à enregistrer des joueurs ?")
                break
            # get all players
            if choice == "2":
                if not json_players:
                    print("la liste est vide, merci de créer des joueurs")
                    self.players_menu()
                    break
                else:
                    data.players_desencoder("all_players")
            # create tournament players list
            if choice == "3":
                if not json_players:
                    print("la liste est vide, merci de créer des joueurs")
                    self.players_menu()
                    break
                if len(json_players) < 8:
                    data.players_desencoder("players")
                    print("il n'y a pas assez de joueurs, merci de créer des joueurs supplémentaires")
                    self.players_menu()
                    break
                if tournament.tournament:
                    if json_tournament_players:
                        print("ce tournoi est selectionné : ")
                        print(tournament.tournament)
                        print("souhaitez-vous lui affilier ces joueurs ? :")
                        data.players_desencoder("tournament_players")
                        status = tournament.stop_tournament("cette association")
                        if status == "stop":
                            data.delete_tournament_player()
                            self.players_menu()
                            break
                        else:
                            data.update_tournament_start(tournament.tournament.name,
                                                         data.players_desencoder("tournament_players"))
                    else:
                        if len(json_tournament_players) < 8:
                            associate_players()
                        print(f"cette liste est enregistrée dans le tournoi {tournament.tournament.name}")
                        data.players_desencoder("tournament_players")
                        status = tournament.stop_tournament("vers le tournoi")
                        if status == "stop":
                            self.players_menu()
                            break
                        else:
                            self.tournament_menu()
                            break
                else:
                    if len(json_tournament_players) < 8:
                        associate_players()
                    status = tournament.stop_tournament("vers le tournoi")
                    if status == "stop":
                        self.players_menu()
                        break
                    else:
                        self.tournament_menu()
                        break
            # get tournament players list
            if choice == "4":
                if not json_tournament_players:
                    print("il n'y a pas de liste enregistrée")
                else:
                    if tournament.tournament:
                        if tournament.tournament.players_list:
                            data.players_desencoder("tournament_players")
                        else:
                            print("ce tournoi est selectionné : ")
                            print(tournament.tournament)
                            print("souhaitez-vous lui affilier ces joueurs ? :")
                            data.players_desencoder("tournament_players")
                            status = tournament.stop_tournament("cette association")
                            if status == "stop":
                                data.delete_tournament_player()
                                self.players_menu()
                                break
                            else:
                                data.update_tournament_start(tournament.tournament.name,
                                                             data.players_desencoder("tournament_players"))
                    else:
                        data.players_desencoder("tournament_players")
            # delete tournament players list
            if choice == "5":
                to_delete = data.delete_tournament_player()
                print(to_delete)
                if not to_delete:
                    print("il n'y a pas de liste enregistrée")
                else:
                    data.players_desencoder("tournament_players")
            if choice == "6":
                self.first_menu()

    def tournament_menu(self):
        choice = 0
        tournament = self.tournament
        data = self.data
        json_tournament = data.tournament
        json_tournament_players = data.tournament_players
        while choice != "1" or "2":
            choice = self.view.tournament_menu()
            if choice == "1":
                tournament.get_tournament()
                print(tournament.tournament)
                to_save = data.tournament_encoder(tournament.tournament)
                data.save_tournament(to_save)
                if not json_tournament_players:
                    print("il n'y a pas de joueurs pour ce tournoi, merci d'en selectionner")
                    self.players_menu()
                    break
                print(tournament.tournament.name)
                print(tournament.tournament)
                tournament.tournament.players_list = data.players_desencoder("tournament_players")
                status = tournament.stop_tournament("avec ces joueurs")
                if status == "stop":
                    self.first_menu()
                    break
                if status == "players_menu":
                    tournament.tournament.players_list = []
                    self.players_menu()
                    break
                else:
                    tournament.tournament.start_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                    data.update_tournament_start(tournament.tournament.name,
                                                 tournament.tournament.players_list, tournament.tournament.start_date)
                    tournament.players = tournament.tournament.players_list
                    tournament.new_tournament()
                    break
            if choice == "2":
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
                        print(tournament.tournament)
                        print("yo", tournament.tournament.players_list)
                        if not tournament.tournament.players_list:
                            if json_tournament_players:
                                tournament.tournament.players_list = data.players_desencoder("tournament_players")
                                status = tournament.stop_tournament("avec ces joueurs")
                                if status == "stop":
                                    self.first_menu()
                                    break
                                if status == "players_menu":
                                    tournament.tournament.players_list = []
                                    data.delete_tournament_player()
                                    self.players_menu()
                                    break
                                else:
                                    data.update_tournament_start(tournament.tournament.name,
                                                                 tournament.tournament.players_list)
                                    tournament.players = tournament.tournament.players_list
                                    # tournament.tournament.start_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                                    tournament.new_tournament()
                                    break
                            else:
                                print("merci de selectionner les joueurs de ce tournoi")
                                self.players_menu()
                        else:
                            tournament.players = tournament.tournament.players_list
                            status = self.tournament.stop_tournament("le tournoi")
                            if status == "stop":
                                break
                            else:
                                print(tournament.players)
                                tournament.tournament.start_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                                print(tournament.tournament)
                                tournament.new_tournament()
                                break

            if choice == "3":
                if not json_tournament:
                    print("pas de tournoi enregistré, merci d'en créer un nouveau")
                    self.tournament_menu()
                    break
                else:
                    data.delete_tournaments()
                    self.first_menu()
                    break

    def data_menu(self):
        choice = 0
        details_choice = 0
        data = self.data
        json_tournament = data.tournament
        json_tournament_players = data.tournament_players
        while choice != "1" or "2" or "3":
            choice = self.view.data_menu()
            if choice == "1":
                if len(json_tournament_players) > 0:
                    data.players_desencoder("all_players")
                else:
                    print("il n'y a pas de joueurs enregistrés")
                    self.data_menu()
            if choice == "2":
                if len(json_tournament) > 0:
                    for i in range(len(json_tournament.all())):
                        print(i + 1, data.tournament_desencoder(json_tournament.all()[i])[0])
                    tournament_choice = self.view.choose_tournament()
                    selected = data.tournament_desencoder(data.get_tournament(tournament_choice))
                    if not selected[2]:
                        print(selected[0], "\nce tournoi n'a pas commencé")
                    else:
                        print(selected)
                        print(selected[0], "\ndate début: ", selected[2], "\ndate fin: ", selected[3])
                    while details_choice != "1" or "2" or "3":
                        details_choice = self.view.data_tournament_menu()
                        if details_choice == "1":
                            print(sorted(selected[6]))
                        if details_choice == "2":
                            print(selected[4])
                        if details_choice == "3":
                            self.data_menu()
                            break
                else:
                    print("il n'y a pas de tournoi enregistré")
                    self.data_menu()
            if choice == "3":
                self.first_menu()
                break
