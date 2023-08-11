class View:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def main_menu():
        choice = input("Menu principal : Tapez le numéro de votre choix : \n"
                       "1 - Menu joueur \n"
                       "2 - Menu tournoi \n"
                       "3 - Menu data \n")
        return choice

    @staticmethod
    def players_menu():
        choice = input("Menu joueurs : Tapez le numéro de votre choix : \n"
                       "1 - Créer des nouveaux joueurs \n"
                       "2 - Voir tous les joueurs \n"
                       "3 - Créer la liste des joueurs du tournoi \n"
                       "4 - Voir la liste des joueurs du tournoi \n"
                       "5 - Effacer la liste de joueurs du tournoi \n"
                       "6 - Retour au menu principal \n")
        return choice

    @staticmethod
    def tournament_menu():
        choice = input("Menu tournoi : Tapez le numéro de votre choix : \n"
                       "1 - Créer un nouveau tournoi \n"
                       "2 - Récupérer tournoi existant \n"
                       "3 - Supprimer les tournois \n"
                       "4 - Retour au menu principal \n")
        return choice

    @staticmethod
    def data_menu():
        choice = input("Menu Data - Tapez le numéro de votre choix : \n"
                       "1 - Afficher tous les joueurs \n"
                       "2 - Afficher tous les tournois \n"
                       "3 - Retour au menu principal \n")
        return choice

    @staticmethod
    def data_tournament_menu(name):
        choice = input(f"Menu Data {name} - Tapez le numéro de votre choix : \n"
                       "1 - Afficher les joueurs de ce tournoi \n"
                       "2 - Afficher les tours du tournoi \n"
                       "3 - Revenir au menu \n")
        return choice

    """def data_players(self):
        if len(self.data.tournament_players) > 0:
            to_print = self.data.players_desencoder("all_players")
            for player in to_print:
                print(player)
        else:
            print("Il n'y a pas de joueurs enregistrés")

    def data_tournament(self):
        details_choice = 0
        if len(self.data.tournament) > 0:
            for i in range(len(self.data.tournament.all())):
                print(i + 1, self.data.tournament_desencoder(self.data.tournament.all()[i])[0])
            tournament_choice = self.choose_tournament()
            selected = self.data.tournament_desencoder(self.data.get_tournament(tournament_choice))
            if not selected[2]:
                print(selected[0], f"\n{selected[1]}", "\nCe tournoi n'a pas commencé")
            else:
                print(selected, "\n", selected[1])
                print(selected[0], "\nDate début: ", selected[2], "\nDate fin: ", selected[3])
            while details_choice != "1" or "2" or "3":
                details_choice = self.data_tournament_menu(selected[0])
                if details_choice == "1":
                    if not selected[6]:
                        print("Il n'y a pas encore de joueurs pour ce tournoi")
                    else:
                        print(sorted(selected[6]))
                if details_choice == "2":
                    if not selected[4]:
                        print("Il n'y a pas encore de tours pour ce tournoi")
                    else:
                        print(selected[4])
                if details_choice == "3":
                    return False
        else:
            print("Il n'y a pas de tournoi enregistré")
            return False"""

    @staticmethod
    def prompt_for_tournament():
        name = input("Tapez le nom du tournoi : ")
        place = input("Tapez le lieu du tournoi : ")
        return name, place

    @staticmethod
    def prompt_for_player():
        first_name = input("Entrer le prenom du joueur : ")
        last_name = input("Entrer le nom du joueur : ")
        birthdate = input("Entrer la naissance du joueur : ")
        return first_name, last_name, birthdate

    @staticmethod
    def get_score(player1, player2):
        score_1 = 2
        score_2 = 2
        while score_1 or score_2 != "0" or "0.5" or "1":
            try:
                score_1 = float(input(f"Entrer le score de {player1} : "))
                score_2 = float(input(f"Entrer le score du {player2} : "))
                break
            except ValueError:
                print("Incorrect. Entrer 0, 0.5 ou 1")
        return score_1, score_2

    @staticmethod
    def continue_or_not(state):
        if state == "avec ces joueurs":
            choice = input(f"Souhaitez-vous continuer {state} ? \n"
                           "1 - Continuer \n"
                           "2 - Pause \n"
                           "3 - Choisir d'autres joueurs \n")
        else:
            choice = input(f"Souhaitez-vous continuer {state} ? \n"
                           "1 - Continuer \n"
                           "2 - Pause \n")
        return choice

    @staticmethod
    def choose_players():
        choice = input("Merci d'entrer le numéro du joueur souhaité : ")
        return choice

    @staticmethod
    def choose_tournament():
        choice = input("Merci d'entrer le numéro du tournoi : ")
        return choice
