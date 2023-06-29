import json


class Datas:
    def __init__(self):
        self.players = {}
        self.tours = []
        self.tournament = []

    def players_encoder(self, player):
        # file = open("players.json", "a+")
        data = {"firstname": player.first_name}
        return data
        # "lastname": player.last_name,
        # "birthdate": player.birthdate}
        # self.players["players"] = data
        # print(self.players)
        # json_object = json.dumps(self.players)
        # file.write(json_object)
