class Player:

    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return str(self)


"""new_player = Player("Jacques", "Richard", "05/06/90")
new_player2 = Player("Michel", "Rdhue", "05/08/95")
new_player3 = Player("René", "chinon", "25/01/78")
new_player.add_player([new_player, new_player2, new_player3])
print("Player.players_list : ", Player.players_list)"""
