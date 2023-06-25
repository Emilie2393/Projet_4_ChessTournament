from Controlers.tournament_controller import TournamentController
from Controlers.main_controller import MainController
from Views.View import View


def main():
    view = View()
    tournament = TournamentController(view)
    menu = MainController(view, tournament)
    menu.first_menu()


main()
