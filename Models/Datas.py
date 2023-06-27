import json


class Datas:
    def __init__(self):
        self.players = {}
        self.tours = []
        self.tournament = []

    def players_encoder(self, player):
        data = {"player ":
                    {"firstname": player.first_name}
                }
        self.players["players"] = data
        json_object = json.dumps(self.players)
        with open("players.json", "w") as outfile:
            outfile.write(json_object)
