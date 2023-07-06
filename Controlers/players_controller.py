from Models.Datas import Data
from Models.Player import Player


class PlayersController:
    players_list = []

    def __init__(self, view):
        self.view = view

    def get_new_players(self):
        name = self.view.prompt_for_player()
        player = Player(name)
        encoder = Data()
        json_format = encoder.players_encoder(player)
        encoder.players_insert(json_format)

    def tournament_players(self, selected):
        get_player = Data()
        selection = get_player.get_datas(selected)
        self.players_list.append(selection["firstname"])
        print(self.players_list)
