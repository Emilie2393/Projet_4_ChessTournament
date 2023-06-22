from Controlers.Controller import Controller
from Views.View import View


def main():
    view = View()
    game = Controller(view)
    game.run()


main()
