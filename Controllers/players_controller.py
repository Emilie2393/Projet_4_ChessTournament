from Models.player import Player


class PlayersController:

    def __init__(self, view, data, tournament):
        self.view = view
        self.data = data
        self.tournament = tournament

    def get_new_players(self):
        name = self.view.prompt_for_player()
        player = Player(name[0], name[1], name[2], name[3])
        self.data.players_serialize(player)

    def tournament_players(self, selected):
        selection = self.data.get_datas(selected)
        print("Votre choix : ", selection)
        return selection

    def see_players(self):
        if not self.data.players:
            print("!-- la liste est vide, merci de créer des joueurs")
        else:
            to_print = self.data.players_deserialize("all_players")
            for player in to_print:
                print(player[0], player[1])

    def create_player(self):
        status = 0
        # register players in json
        while status != "stop":
            self.get_new_players()
            self.data.players_deserialize("all_players")
            status = self.tournament.stop_tournament("à enregistrer des joueurs ?")

    def associate_players(self):
        # associate players with tournament player list
        while len(self.data.tournament_players) < 8:
            for i in range(len(self.data.players.all())):
                print(i + 1, self.data.players.all()[i])
            players_choice = self.view.choose_players()
            name = self.tournament_players(players_choice)
            # if a player is already in list
            if name in self.data.tournament_players.all():
                print("!-- Ce joueur est déjà dans la liste des joueurs du tournoi")
            else:
                self.data.save_tournament_player(name)
        self.tournament.players = self.data.players_deserialize("tournament_players")

    def init_tournament_players(self):
        if not self.data.players:
            print("!-- La liste est vide, merci de créer des joueurs")
        if len(self.data.players) < 8:
            print("Il y a actuellement", len(self.data.players), "joueurs enregistrés")
            print("!-- Il n'y a pas assez de joueurs, merci de créer des joueurs supplémentaires")
        if len(self.data.tournament_players) < 8 <= len(self.data.players):
            self.associate_players()
            print("Vous pouvez maintenant démarrer un tournoi avec ces joueurs")

    def see_tournament_players(self):
        if not self.data.tournament_players:
            print("!-- il n'y a pas de liste enregistrée")
        else:
            print(self.data.players_deserialize("tournament_players"))

    def del_tournament_players(self):
        self.data.delete_tournament_player()

    def del_players(self):
        self.data.delete_player()
