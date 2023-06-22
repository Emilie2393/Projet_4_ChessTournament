class View:
    def prompt_for_player(self):
        """Prompt for a name."""
        first_name = input("tapez le prenom du joueur : ")
        last_name = input("tapez le nom du joueur : ")
        birthdate = input("tapez la naissance du joueur : ")
        if not first_name:
            return None
        if not last_name:
            return None
        if not birthdate:
            return None
        return first_name, last_name, birthdate

    def get_score(self, player1, player2):
        score_1 = int(input(f"tapez le score de {player1} : "))
        score_2 = int(input(f"tapez le score du {player2} : "))
        return score_1, score_2

    def next_tour(self):
        wait = input("Tapez Entrée quand vous êtes prêts pour le prochain round : ")
