import random


class Card:
    def __init__(self, attack, health, is_bubbled=False, is_poison=False):
        self.attack = attack
        self.health = health
        self.is_bubbled = is_bubbled
        self.is_poison = is_poison
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
        other.takes_damage(self)
        self.takes_damage(other)

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
        self.is_dead = True


class Game:
    def __init__(self, lang='ru'):
        self.lang = lang
        self.top_board = []
        self.bottom_board = []
        self.is_top_first = True

    def run(self):
        while self.top_board and self.bottom_board:
            attacker, attacked, board, opp_board = self.next_card()

            print(f"{attacker} атакует {attacked}: -> ", end='')
            attacker.do_attack(attacked)
            print(f"{attacker}, {attacked}")

            if attacker.is_dead:
                board.remove(attacker)
            if attacked.is_dead:
                opp_board.remove(attacked)

            print(self.top_board)
            print(self.bottom_board)
            print('--' * 30)

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
