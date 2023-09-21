import pygame
import time
from models import Game
import custom_cards as cc

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CARD_WIDTH = 130
CARD_HEIGHT = 170

GREEN = (0, 255, 0)
GREY = (100, 100, 100)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
font1 = pygame.font.Font('freesansbold.ttf', 14)
font2 = pygame.font.Font('freesansbold.ttf', 24)

game = Game()
game.top_board = [cc.Annoy_o_Tron(), cc.Annoy_o_Tron(), cc.Dozy_Whelp()]
game.bottom_board = [cc.Dozy_Whelp(), cc.Annoy_o_Tron(), cc.Annoy_o_Tron()]

# screen is a Surface object
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True


def draw_board(board, screen, y):
    pad = 5
    for i in range(len(board)):
        card = board[i]
        if card.is_bubbled:
            card_color = GREEN
        else:
            card_color = GREY

        attack_text = font2.render(str(card.attack), True, BLACK, card_color)
        attackRect = attack_text.get_rect(bottomleft=(pad, CARD_HEIGHT - pad))

        health_text = font2.render(str(card.health), True, BLACK, card_color)
        healthRect = health_text.get_rect(bottomright=(CARD_WIDTH - pad,
                                                       CARD_HEIGHT - pad))

        name = font1.render(card.name, True, BLACK, card_color)
        nameRect = name.get_rect()
        nameRect.center = (CARD_WIDTH // 2, CARD_HEIGHT // 2)

        x = 20 + (i * (CARD_WIDTH + 20))
        card_surf = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        card_surf.fill(card_color)
        card_surf.blit(attack_text, attackRect)
        card_surf.blit(health_text, healthRect)
        card_surf.blit(name, nameRect)
        screen.blit(card_surf, (x, y))


screen.fill((255, 255, 255))
draw_board(game.top_board, screen, 20)
draw_board(game.bottom_board, screen, 220)
pygame.display.flip()
time.sleep(3)
while running and game.top_board and game.bottom_board:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    attacker, attacked, board, opp_board = game.next_card()
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

    draw_board(game.top_board, screen, 20)
    draw_board(game.bottom_board, screen, 220)
    pygame.display.flip()
    time.sleep(2)

pygame.quit()
