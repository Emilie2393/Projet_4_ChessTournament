from Models.data import Data
from Models.player import Player


class PlayersController:

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
        print(selection)
        return selection
        """self.players_list.append(selection["firstname"])
        print(self.players_list)"""
