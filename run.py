from models import Card, Game
import curses
import custom_cards as cc


def main(stdscr):
    FPS = 60
    # Инициализация curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000 // FPS)

    game = Game(stdscr)
    game.top_board = [cc.Annoy_o_Tron(), cc.Annoy_o_Tron(), cc.Dozy_Whelp()]
    game.bottom_board = [cc.Dozy_Whelp(), cc.Annoy_o_Tron(), cc.Annoy_o_Tron()]
    game.run_in_terminal()


if __name__ == '__main__':
    curses.wrapper(main)
