class Player:

    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.birthdate}"

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        return self.first_name[key]
