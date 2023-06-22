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

    def get_score(self):
        score_1 = input("tapez le score du joueur 1 : ")
        score_2 = input("tapez le score du joueur 2 : ")
        return score_1, score_2
