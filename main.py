from Controllers.tournament_controller import TournamentController
from Controllers.players_controller import PlayersController
from Controllers.main_controller import MainController
from Controllers.reports_controller import ReportsController
from Models.data import Data
from Views.View import View


def main():
    data = Data()
    view = View()
    tournament = TournamentController(view, data)
    players = PlayersController(view, data, tournament)
    reports = ReportsController(view, data)
    menu = MainController(view, tournament, players, data, reports)
    menu.first_menu()


main()
