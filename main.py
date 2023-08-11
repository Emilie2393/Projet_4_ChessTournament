from Controllers.tournament_controller import TournamentController
from Controllers.players_controller import PlayersController
from Controllers.main_controller import MainController
from Models.data import Data
from Views.View import View


# main menu
# Datas = data
def main():
    data = Data()
    view = View(data)
    tournament = TournamentController(view)
    players = PlayersController(view)
    menu = MainController(view, tournament, players, data)
    menu.first_menu()


main()
