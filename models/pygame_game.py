import pygame
from models.base_game import Game
from models.pygame_card import PyGameCard
from time import sleep

CARD_WIDTH = 130
CARD_HEIGHT = 170
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class PyGame(Game):
    def __init__(self, scr=None, lang='ru'):
        super().__init__(scr=scr, lang=lang)
        pygame.init()
        self.text_font = pygame.font.Font('freesansbold.ttf', 14)
        self.stats_font = pygame.font.Font('freesansbold.ttf', 24)
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    def run(self):
        running = True
        self.screen.fill((255, 255, 255))
        self.draw_board(self.screen, self.top_board, 20)
        self.draw_board(self.screen, self.bottom_board, 220)
        pygame.display.flip()
        while self.top_board and self.bottom_board and running:
            sleep(2)
            self.screen.fill((255, 255, 255))
            attacker, attacked, board, opp_board = self.next_card()

            # run new iteration if attacker cannot attack
            if not attacker.can_attack:
                continue

            attacker.do_attack(attacked)

            if attacker.health <= 0:
                index = board.index(attacker)
                summon = attacker.die()
                if summon is not None:
                    board[index] = summon
                else:
                    board.pop(index)

            if attacked.health <= 0:
                index = opp_board.index(attacked)
                summon = attacked.die()
                if summon is not None:
                    opp_board[index] = summon
                else:
                    opp_board.pop(index)

            self.draw_board(self.screen, self.top_board, 20)
            self.draw_board(self.screen, self.bottom_board, 220)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        sleep(15)
        pygame.quit()

    def draw_board(self, surface, board, y):
        for i in range(len(board)):
            card_surf = board[i].get_card_surface()
            x = 20 + (i * (CARD_WIDTH + 20))
            surface.blit(card_surf, (x, y))
