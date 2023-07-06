from Controlers.tournament_controller import TournamentController
from Controlers.players_controller import PlayersController
from Controlers.main_controller import MainController
from Models.Datas import Data
from Views.View import View


def main():
    view = View()
    tournament = TournamentController(view)
    players = PlayersController(view)
    data = Data()
    menu = MainController(view, tournament, players, data)
    menu.first_menu()


main()
