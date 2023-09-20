import random
import curses
from time import sleep


class Card:
    def __init__(self, attack, health, is_bubbled=False, is_poison=False,
                 is_reborn=False, is_taunt=False):
        self.attack = attack
        self.health = health
        self.is_bubbled = is_bubbled
        self.is_poison = is_poison
        self.is_reborn = is_reborn
        self.is_taunt = is_taunt

        self.is_dead = False
        self.attacked = False

    def __repr__(self):
        atk_info = str(self.attack)
        if self.is_poison:
            atk_info += 'p'

        health_info = str(self.health)
        if self.is_bubbled:
            health_info += 'b'

        return f"|{atk_info: <3}|{health_info: >3}|"

    def __str__(self):
        atk_info = str(self.attack)
        if self.is_poison:
            atk_info += 'p'

        health_info = str(self.health)
        if self.is_bubbled:
            health_info += 'b'

        s1 = '\u250c' + '\u2500' * 7 + '\u2510' + '\n'
        s2 = '\u2502' + ' ' * 7 + '\u2502' + '\n'
        s3 = '\u2502' + ' ' * 7 + '\u2502' + '\n'
        s4 = f"\u2502{atk_info: <3}|{health_info: >3}\u2502" + '\n'
        s5 = '\u2514' + '\u2500' * 7 + '\u2518'

        return s1 + s2 + s3 + s4 + s5

    def do_attack(self, other):
        self.before_attack(other)
        other.before_attacked(self)

        other.takes_damage(self)
        self.takes_damage(other)

    def before_attack(self, other):
        pass

    def before_attacked(self, other):
        pass

    def takes_damage(self, other):
        if self.is_bubbled:
            self.is_bubbled = False
            return

        if other.is_poison:
            self.health = 0
            self.die()
            return

        self.health -= other.attack
        if self.health <= 0:
            self.die()

    def die(self):
        if self.reborn:
            self.reborn = False
            pass
        self.is_dead = True


class Game:
    def __init__(self, scr, lang='ru'):
        self.lang = lang
        self.top_board = []
        self.bottom_board = []
        self.is_top_first = True
        self.scr = scr

    def run_in_terminal(self):
        self.print_board()
        self.scr.refresh()
        while self.top_board and self.bottom_board:
            sleep(1)
            attacker, attacked, board, opp_board = self.next_card()
            attacker.do_attack(attacked)

            if attacker.is_dead:
                board.remove(attacker)
            if attacked.is_dead:
                opp_board.remove(attacked)

            self.scr.clear()
            self.print_board()
            self.scr.refresh()

        sleep(15)

    def print_board(self):
        card_num = -1
        for card in self.top_board:
            card_num += 1
            sprite = list(str(card).split('\n'))
            for i in range(len(sprite)):
                self.scr.addstr(i + 1, card_num * 9, sprite[i])

        card_num = -1
        for card in self.bottom_board:
            card_num += 1
            sprite = list(str(card).split('\n'))
            for i in range(len(sprite)):
                self.scr.addstr(i + 15, card_num * 9, sprite[i])

    def set_random_board(self):
        for i in range(14):
            card = self.generate_card()
            if i % 2 == 0:
                self.top_board.append(card)
            else:
                self.bottom_board.append(card)

    def generate_card(self):
        atk = random.randint(1, 16)
        hlt = random.randint(1, 20)

        prob1 = random.randint(1, 10)
        is_bub = False
        if prob1 == 5:
            is_bub = True

        prob2 = random.randint(1, 15)
        is_pois = False
        if prob2 == 5:
            is_pois = True

        card = Card(atk, hlt, is_bubbled=is_bub, is_poison=is_pois)
        return card

    def next_card(self):
        '''Returns the card that must attack and the one that is attacked'''
        if self.is_top_first:
            board = self.top_board
            opposite_board = self.bottom_board
        else:
            board = self.bottom_board
            opposite_board = self.top_board

        for card in board:
            if not card.attacked:
                card.attacked = True
                self.is_top_first = not self.is_top_first
                return (card, random.choice(opposite_board), board,
                        opposite_board)

        for card in board:
            card.attacked = False

        self.is_top_first = not self.is_top_first
        return (board[0], random.choice(opposite_board), board,
                opposite_board)
