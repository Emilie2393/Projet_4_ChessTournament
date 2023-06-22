from Controlers.Controller import Controller
from Views.Players import View


def main():
    view = View()
    game = Controller(view)
    game.run()


main()
