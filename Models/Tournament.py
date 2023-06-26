class Tournament:
    tours_list = []
    players_list = []

    def __init__(self, name, place, start_date, end_date, rounds_nb=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_nb = rounds_nb
        self.round = 0

    def __str__(self):
        return f"{self.name, self.place, self.start_date, self.end_date, self.rounds_nb, self.round}"

    def __repr__(self):
        return str(self)

    def add_tour(self, new):
        self.tours_list.append(new)
