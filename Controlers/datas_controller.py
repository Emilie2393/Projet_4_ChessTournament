

class DataController:
    players = {}

    def player_file(self, player, i):
        self.players[f"test{i}"] = player
        print(len(self.players))
