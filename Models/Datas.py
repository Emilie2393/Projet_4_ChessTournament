from tinydb import TinyDB, Query


class Data:
    db = TinyDB('chess.json')
    players = db.table('players')

    def players_encoder(self, player):
        data = {"firstname": player.first_name}
        return data

    def players_list(self, player):
        self.players.insert(player)
        print(self.players.all())

    def get_datas(self, name):
        data = self.players.get(doc_id=name)
        return data

    def save_tournament_player(self, players_list):
        tournament_players = self.db.table('tournament_players')
        for i in range(len(players_list)):
            tournament_players.insert({"firstname": players_list[i]})


