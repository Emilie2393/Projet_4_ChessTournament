from Controlers.tournament_controller import TournamentController
from Controlers.players_controller import PlayersController
from Controlers.main_controller import MainController
from Views.View import View


def main():
    view = View()
    tournament = TournamentController(view)
    players = PlayersController(view)
    menu = MainController(view, tournament, players)
    menu.first_menu()


main()
