import random


class Card:
    def __init__(self, attack, health, is_bubbled=False, is_poison=False):
        self.attack = attack
        self.health = health
        self.is_bubbled = is_bubbled
        self.is_poison = is_poison

    def __repr__(self):
        atk_info = str(self.attack)
        if self.is_poison:
            atk_info += 'p'

        health_info = str(self.health)
        if self.is_bubbled:
            health_info += 'b'

        return f"({atk_info}-{health_info})"

    def do_attack(self, other):
        other.takes_damage(self)
        self.takes_damage(other)

    def takes_damage(self, other):
        if self.is_bubbled:
            self.is_bubbled = False
            return

        if other.is_poison:
            self.health = 0
            return

        self.health -= other.attack


class Game:
    def __init__(self, lang='ru'):
        self.lang = lang
        self.top_board = []
        self.bottom_board = []

    def run(self):
        top = iter(self.top_board)
        bottom = iter(self.bottom_board)
        while True:
            crd_top = next(top)
            crd_attacked = random.choice(self.bottom_board)
            print(f"{crd_top} атакует {crd_attacked}: -> ", end='')
            crd_top.do_attack(crd_attacked)
            print(f"{crd_top}, {crd_attacked}")

            if crd_top.health <= 0:
                self.top_board.remove(crd_top)
            if crd_attacked.health <= 0:
                self.bottom_board.remove(crd_attacked)

            print(self.top_board)
            print(self.bottom_board)
            print('--' * 30)

            '''
            crd_btm = next(bottom)
            print(current)
            '''

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
