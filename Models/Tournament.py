class Tournament:
    tours_list = []

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)

    def add_tour(self, new):
        for i in new:
            self.tours_list.append(i)
        return self.name, self.tours_list
