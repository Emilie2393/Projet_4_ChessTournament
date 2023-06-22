#from Match import match_one, match_two


class Tour:
    match_list = []

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}, {self.match_list}"

    def __repr__(self):
        return str(self)

    def add_match(self, new):
        self.match_list.append(new)


"""round1 = Tour("Round 1")
test = round1.add_match([match_one, match_two])
print("nom, Tour.add_match : ", test)"""
