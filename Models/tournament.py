class Tournament:

    def __init__(self, name, place, start_date, end_date, tours_list, round, players_list, scores,
                 prev_games, rounds_nb=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.tours_list = tours_list
        self.round = round
        self.players_list = players_list
        self.scores = scores
        self.prev_games = prev_games
        self.rounds_nb = rounds_nb

    def __str__(self):
        return f"{self.name}, {self.place}, {self.start_date}, {self.end_date}, {self.tours_list}" \
               f"{self.round}, {self.players_list}, {self.scores}, {self.rounds_nb}"

    def __repr__(self):
        return str(self)
