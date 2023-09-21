import random
import curses
from time import sleep


class Card:
    def __init__(self, attack=None, health=None):
        self.attack = attack if attack is not None else random.randint(1, 15)
        self.health = health if health is not None else random.randint(1, 18)

        self.is_bubbled = False
        self.is_poison = False
        self.is_reborn = False
        self.is_taunt = False
        self.can_attack = True if self.attack > 0 else False
        self.lost_hp = False
        self.name = 'card'

        self.is_dead = False
        self.attacked = False

    def __repr__(self):
        atk_info = str(self.attack)
        if self.is_poison:
            atk_info += 'p'

        health_info = str(self.health)
        if self.is_bubbled:
            health_info += 'b'
        if self.is_reborn:
            health_info += 'r'
        if self.is_taunt:
            health_info += 't'

        return f"|{atk_info: <3}|{health_info: >3}|"

    def __str__(self):
        atk_info = str(self.attack)
        if self.is_poison:
            atk_info += 'p'

        health_info = str(self.health)
        if self.is_bubbled:
            health_info += 'b'
        if self.is_reborn:
            health_info += 'r'
        if self.is_taunt:
            health_info += 't'

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
            self.lost_hp = True
            return

        self.health -= other.attack
        self.lost_hp = True

    def die(self):
        '''If summons something after death, returns it. Otherwise
        returns None'''
        self.is_dead = True

        if self.is_reborn:
            self.is_reborn = False
            reborned_card = self.__class__()
            reborned_card.health = 1
            return reborned_card

        return None


class Game:
    def __init__(self, scr=None, lang='ru'):
        self.lang = lang
        self.top_board = []
        self.bottom_board = []
        self.is_top_first = True
        self.scr = scr

    def run_in_terminal(self):
        self.print_board()
        self.scr.refresh()
        while self.top_board and self.bottom_board:
            sleep(4)
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
                if card.lost_hp:
                    self.scr.addstr(i + 1, card_num * 9, sprite[i], curses.A_DIM)
                else:
                    self.scr.addstr(i + 1, card_num * 9, sprite[i])

        card_num = -1
        for card in self.bottom_board:
            card_num += 1
            sprite = list(str(card).split('\n'))
            for i in range(len(sprite)):
                if card.lost_hp:
                    self.scr.addstr(i + 15, card_num * 9, sprite[i], curses.A_DIM)
                else:
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

        card = Card(attack=atk, health=hlt)
        card.is_bubbled = is_bub
        card.is_poison = is_pois
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
            # not done
            if not card.attacked and card.attack >= 0:
                card.attacked = True
                self.is_top_first = not self.is_top_first
                return (card, random.choice(opposite_board), board,
                        opposite_board)

        for card in board:
            card.attacked = False

        self.is_top_first = not self.is_top_first
        return (board[0], random.choice(opposite_board), board,
                opposite_board)
