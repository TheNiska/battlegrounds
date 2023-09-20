from models import Card, Game
import curses


def main(stdscr):
    FPS = 60
    # Инициализация curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1000 // FPS)

    game = Game(stdscr)
    game.set_random_board()
    game.run()


if __name__ == '__main__':
    curses.wrapper(main)
