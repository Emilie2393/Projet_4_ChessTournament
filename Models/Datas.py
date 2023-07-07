from tinydb import TinyDB, Query, where
from tinydb.operations import delete


class Data:
    db = TinyDB('chess.json')
    players = db.table('players')
    tournament_players = db.table('tournament_players')
    tournament = db.table('tournament')

    def players_encoder(self, player):
        data = {"firstname": player.first_name}
        return data

    def players_desencoder(self, query):
        players = []
        if query == "all_players":
            for i in self.players:
                players.append(i["firstname"])
            print(sorted(players))
        if query == "tournament_players":
            for i in self.tournament_players:
                players.append(i["firstname"])
            print(sorted(players))
        return sorted(players)

    def players_insert(self, player):
        self.players.insert(player)

    def get_datas(self, name):
        data = self.players.get(doc_id=name)
        return data

    def get_tournament(self, name):
        data = self.tournament.get(doc_id=name)
        return data

    def save_tournament_player(self, players_list):
        if self.db.table("tournament_player") != {}:
            self.db.table('tournament_players').truncate()
        else:
            pass
        for i in range(len(players_list)):
            self.tournament_players.insert({"firstname": players_list[i]})

    def check_tournament_player(self):
        if not self.tournament_players.all():
            return False
        else:
            return True

    def delete_tournament_player(self):
        if not self.tournament_players.all():
            return False
        else:
            self.tournament_players.truncate()

    def tournament_encoder(self, tournament):
        data = {"name": tournament.name, "place": tournament.place, "start_date": tournament.start_date,
                "end_date": tournament.end_date, "rounds_nb": tournament.rounds_nb,
                "round_in_progress": tournament.round, "players_list": tournament.players_list,
                "tours_list": tournament.tours_list}
        return data

    def tournament_desencoder(self, tournament):
        name = tournament["name"]
        place = tournament["place"]
        start_date = tournament["start_date"]
        end_date = tournament["end_date"]
        rounds_nb = tournament["rounds_nb"]
        round_in_progress = tournament["round_in_progress"]
        players_list = tournament["players_list"]
        tours_list = tournament["tours_list"]
        data = [name, place, start_date, end_date, rounds_nb, round_in_progress, players_list, tours_list]
        return

    def save_tournament(self, tournament):
        self.tournament.insert(tournament)

    def update_tournament(self, name, players):
        data = Query()
        self.tournament.update({"players_list": players}, data["name"] == f"{name}")

    def delete_tournaments(self):
        self.tournament.truncate()
