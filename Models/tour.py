

class Tour:

    def __init__(self, name):
        self.matches = []
        self.name = name

    def __str__(self):
        return f"{self.name}, {self.matches}"

    def __repr__(self):
        return str(self)

    def add_match(self, new):
        self.matches.append(new)
