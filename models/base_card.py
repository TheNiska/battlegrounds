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
            reborned_card = self.__class__()
            reborned_card.health = 1
            reborned_card.is_reborn = False
            return reborned_card

        return None
