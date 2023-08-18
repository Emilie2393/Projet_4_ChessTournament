class ReportsController:

    def __init__(self, view, data):
        self.view = view
        self.data = data

    def data_players(self):
        if len(self.data.tournament_players) > 0:
            to_print = self.data.players_deserialize("all_players")
            for player in to_print:
                self.view.show_msg(player)
        else:
            self.view.show_msg("Il n'y a pas de joueurs enregistrés")

    def data_tournament(self):
        details_choice = 0
        if len(self.data.tournament) > 0:
            for i in range(len(self.data.tournament.all())):
                self.view.show_msg(i + 1, self.data.tournament_deserialize(self.data.tournament.all()[i])[0])
            tournament_choice = self.view.choose_tournament()
            selected = self.data.tournament_deserialize(self.data.get_tournament(tournament_choice))
            if not selected[2]:
                self.view.show_msg(selected[0], f"\n{selected[1]}", "\nCe tournoi n'a pas commencé")
            else:
                self.view.show_msg(selected, "\n", selected[1])
                self.view.show_msg(selected[0], "\nDate début: ", selected[2], "\nDate fin: ", selected[3])
            while details_choice != "1" or "2" or "3":
                details_choice = self.view.data_tournament_menu(selected[0])
                if details_choice == "1":
                    if not selected[6]:
                        self.view.show_msg("Il n'y a pas encore de joueurs pour ce tournoi")
                    else:
                        self.view.show_msg(sorted(selected[6]))
                if details_choice == "2":
                    if not selected[4]:
                        self.view.show_msg("Il n'y a pas encore de tours pour ce tournoi")
                    else:
                        for f in selected[4]:
                            self.view.show_msg(f)
                if details_choice == "3":
                    return
        else:
            self.view.show_msg("Il n'y a pas de tournoi enregistré")
            return
