from models import Card, Game


def main():
    game = Game()
    game.set_random_board()
    print(game.top_board)
    print(game.bottom_board)
    print('------' + 'Game Started' + '------')
    game.run()


if __name__ == '__main__':
    main()
