from tinydb import TinyDB, Query
from Views.View import View


class Data:
    db = TinyDB('chess.json')
    players = db.table('players')
    tournament_players = db.table('tournament_players')
    tournament = db.table('tournament')
    tours_to_save = []
    scores = {}
    prev_games = []

    def players_serialize(self, player):
        data = {"firstname": player.first_name, "lastname": player.last_name, "birthdate": player.birthdate,
                "code": player.code}
        self.players.insert(data)
        return data

    def players_deserialize(self, query):
        players = []
        if query == "all_players":
            for i in self.players:
                players.append([i["firstname"], i["lastname"], i["birthdate"], i["code"]])
        if query == "tournament_players":
            for i in self.tournament_players:
                players.append(i["firstname"] + " " + i["lastname"])
        return sorted(players)

    def tours_list_serialize(self, tour, name):
        data = Query()
        serialized_tours = []
        for i in range(len(tour.matches)):
            player1 = tour.matches[i][0]
            player2 = tour.matches[i][1]
            game = {player1[0]: player1[1], player2[0]: player2[1]}
            serialized_tours.append(game)
        new_tour = {tour.name: serialized_tours}
        self.tours_to_save.append(new_tour)
        self.tournament.update({"tours_list": self.tours_to_save}, data["name"] == f"{name}")

    def get_datas(self, name):
        data = self.players.get(doc_id=name)
        return data

    def get_tournament(self, name):
        data = self.tournament.get(doc_id=name)
        return data

    def save_tournament_player(self, player):
        if len(self.db.table("tournament_player")) < 8:
            self.tournament_players.insert(player)
            View.show_msg(self.tournament_players.all())
        else:
            View.show_msg("Complet")

    def delete_tournament_player(self):
        if not self.tournament_players.all():
            View.show_msg("!-- Il n'y a pas de pas de liste à supprimer")
        else:
            self.tournament_players.truncate()

    def delete_player(self):
        if not self.players.all():
            View.show_msg("!-- Il n'y a pas de pas de liste à supprimer")
        else:
            self.players.truncate()

    def tournament_serialize(self, tournament):
        data = {"name": tournament.name, "place": tournament.place, "start_date": tournament.start_date,
                "end_date": tournament.end_date, "tours_list": tournament.tours_list,
                "round": tournament.round, "players_list": tournament.players_list, "scores": tournament.scores,
                "prev_games": tournament.prev_games, "rounds_nb": tournament.rounds_nb}
        self.tournament.insert(data)

    def tournament_deserialize(self, tournament):
        name = tournament["name"]
        place = tournament["place"]
        start_date = tournament["start_date"]
        end_date = tournament["end_date"]
        rounds_nb = tournament["rounds_nb"]
        round = tournament["round"]
        players_list = tournament["players_list"]
        scores = tournament["scores"]
        prev_games = tournament["prev_games"]
        tours_list = tournament["tours_list"]
        data = [name, place, start_date, end_date, tours_list, round, players_list, scores, prev_games, rounds_nb]
        return data

    def update_tournament_data(self, name, players, start=0, end=0):
        data = Query()
        self.tournament.update({"players_list": players}, data["name"] == f"{name}")
        if start != 0:
            self.tournament.update({"start_date": start}, data["name"] == f"{name}")
        if end != 0:
            self.tournament.update({"end_date": end}, data["name"] == f"{name}")

    def update_tournament_tours(self, name, scores, prev_games, tour_nb):
        data = Query()
        self.tournament.update({"scores": scores}, data["name"] == f"{name}")
        self.tournament.update({"prev_games": prev_games}, data["name"] == f"{name}")
        self.tournament.update({"round": tour_nb}, data["name"] == f"{name}")

    def check_tournament(self, name):
        data = Query()
        result = self.tournament.search(data["name"] == f"{name}")
        return result

    def delete_tournaments(self):
        self.tournament.truncate()
