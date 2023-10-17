import pygame
from models.base_card import Card

GREEN = (0, 255, 0)
GREY = (100, 100, 100)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PAD = 5


class PyGameCard(Card):
    def __init__(self, stats_font=None, text_font=None,
                 attack=None, health=None):
        super().__init__(attack=attack, health=health)
        self.stats_font = stats_font
        self.text_font = text_font
        self.center = None

    def get_card_surface(self, card_width=130, card_height=170):
        card_surf = pygame.Surface((card_width, card_height))
        if self.is_bubbled:
            card_color = GREEN
        else:
            card_color = GREY
        card_surf.fill(card_color)

        if self.stats_font and self.text_font:
            attack_text = self.stats_font.render(str(self.attack), True,
                                                 BLACK, card_color)
            attackRect = attack_text.get_rect(bottomleft=(PAD,
                                              card_height - PAD))

            health_text = self.stats_font.render(str(self.health), True,
                                                 BLACK, card_color)
            healthRect = health_text.get_rect(bottomright=(card_width - PAD,
                                                           card_height - PAD))

            name = self.text_font.render(self.name, True, BLACK, card_color)
            nameRect = name.get_rect()
            nameRect.center = (card_width // 2, card_height // 2)

            card_surf.blit(attack_text, attackRect)
            card_surf.blit(health_text, healthRect)
            card_surf.blit(name, nameRect)
        return card_surf
