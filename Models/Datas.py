from tinydb import TinyDB, Query


class Data:
    db = TinyDB('chess.json')
    players = db.table('players')
    tournament_players = db.table('tournament_players')

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



    def players_insert(self, player):
        self.players.insert(player)

    def get_datas(self, name):
        data = self.players.get(doc_id=name)
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



