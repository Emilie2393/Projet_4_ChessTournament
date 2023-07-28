from tinydb import TinyDB, Query


class Data:
    db = TinyDB('chess.json')
    players = db.table('players')
    tournament_players = db.table('tournament_players')
    tournament = db.table('tournament')
    tours_to_save = []
    scores = []
    prev_games = []

    def players_encoder(self, player):
        data = {"firstname": player.first_name, "lastname": player.last_name, "birthdate": player.birthdate}
        return data

    def players_desencoder(self, query):
        players = []
        if query == "all_players":
            for i in self.players:
                players.append([i["firstname"], i["lastname"], i["birthdate"]])
            print(sorted(players))
        if query == "tournament_players":
            for i in self.tournament_players:
                players.append(i["firstname"] + " " + i["lastname"])
            print(sorted(players))
        return sorted(players)

    def tours_list_encoder(self, name, tour):
        data = {name: tour}
        self.tours_to_save.append(data)
        print("to_savedata", self.tours_to_save)

    def tours_list_insert(self, tours, name):
        data = Query()
        self.tournament.update({"tours_list": tours}, data["name"] == f"{name}")

    def players_insert(self, player):
        self.players.insert(player)

    def get_datas(self, name):
        data = self.players.get(doc_id=name)
        return data

    def get_tournament(self, name):
        data = self.tournament.get(doc_id=name)
        return data

    def save_tournament_player(self, player):
        if len(self.db.table("tournament_player")) < 8:
            self.tournament_players.insert(player)
            print(self.tournament_players.all())
        else:
            print("complet")

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
                "end_date": tournament.end_date, "tours_list": tournament.tours_list,
                "round": tournament.round, "players_list": tournament.players_list, "scores": tournament.scores,
                "prev_games": tournament.prev_games, "rounds_nb": tournament.rounds_nb}
        return data

    def tournament_desencoder(self, tournament):
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

    def save_tournament(self, tournament):
        data = Query()
        print("save", tournament)
        if tournament["tours_list"]:
            self.tournament.update({"tours_list": tournament["tours_list"]}, data["name"] == f"{tournament['name']}")
        else:
            self.tournament.insert(tournament)

    def update_tournament_start(self, name, players, start=0):
        data = Query()
        self.tournament.update({"players_list": players}, data["name"] == f"{name}")
        if start != 0:
            self.tournament.update({"start_date": start}, data["name"] == f"{name}")

    def update_tournament_tours(self, name, scores, prev_games, tour_nb):
        print(self.scores)
        data = Query()
        self.tournament.update({"scores": scores}, data["name"] == f"{name}")
        self.tournament.update({"prev_games": prev_games}, data["name"] == f"{name}")
        self.tournament.update({"round": tour_nb}, data["name"] == f"{name}")
        print(self.tournament.all())

    def check_tournament(self, name):
        data = Query()
        result = self.tournament.search(data["name"] == f"{name}")
        return result

    def find_full_player(self, name):
        split_name = name.split()
        result = self.players.search(Query().fragment({'firstname': split_name[0], 'lastname': split_name[1]}))
        return result

    def delete_tournaments(self):
        self.tournament.truncate()
