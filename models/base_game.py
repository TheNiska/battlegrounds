import random
import curses
from time import sleep


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
