class View:

    def main_menu(self):
        choice = input("selectionner votre choix : \n"
                       "1 - menu joueur \n"
                       "2 - menu tournoi \n"
                       "3 - menu datas \n")
        return choice

    def players_menu(self):
        choice = input("selectionner votre choix : \n"
                       "1 - créer des nouveaux joueurs \n"
                       "2 - voir tous les joueurs \n"
                       "3 - créer la liste des joueurs du tournoi \n"
                       "4 - voir la liste des joueurs du tournoi \n"
                       "5 - effacer la liste de joueurs du tournoi \n"
                       "6 - retour au menu principal \n")
        return choice

    def tournament_menu(self):
        choice = input("selectionner votre choix : \n"
                       "1 - créer un nouveau tournoi \n"
                       "2 - récupérer tournoi existant \n")
        return choice

    def prompt_for_tournament(self):
        name = input("tapez le nom du tournoi : ")
        place = input("tapez le lieu du tournoi : ")
        start_date = input("tapez la date de départ du tournoi : ")
        end_date = input("tapez la date de fin du tournoi : ")
        rounds_nb = input("tapez le nombre de rounds du tournoi : ")
        return name, place, start_date, end_date, rounds_nb


    def prompt_for_player(self):
        first_name = input("tapez le prenom du joueur : ")
        # last_name = input("tapez le nom du joueur : ")
        # birthdate = input("tapez la naissance du joueur : ")
        if not first_name:
            return None
        """if not last_name:
            return None
        if not birthdate:
            return None"""
        return first_name

    def get_score(self, player1, player2):
        score_1 = float(input(f"tapez le score de {player1} : "))
        score_2 = float(input(f"tapez le score du {player2} : "))
        return score_1, score_2

    def next_tour(self):
        wait = input("Tapez Entrée quand vous êtes prêts pour le prochain round : ")

    def continue_or_not(self, state):
        choice = input(f"souhaitez-vous continuer {state} ? \n"
                       "1 - continuer \n"
                       "2 - pause \n")
        return choice

    def choose_players(self):
        choice = input("merci d'inscrire le numéro du joueur souhaité : ")
        return choice
