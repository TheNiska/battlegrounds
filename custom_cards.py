from models import Card


class Annoy_o_Tron(Card):
    def __init__(self):
        self.attack = 1
        self.health = 2
        self.is_bubbled = True
        self.is_poison = False
        self.is_reborn = False
        self.is_taunt = True

        self.is_dead = False
        self.attacked = False


class Dozy_Whelp(Card):
    def __init__(self):
        self.attack = 0
        self.health = 3
        self.is_bubbled = False
        self.is_poison = False
        self.is_reborn = False
        self.is_taunt = True

        self.is_dead = False
        self.attacked = False

    def before_attacked(self, other):
        self.attack += 1


class Micro_Mummy(Card):
    def __init__(self):
        self.attack = 1
        self.health = 2
        self.is_bubbled = False
        self.is_poison = False
        self.is_reborn = True
        self.is_taunt = False

        self.is_dead = False
        self.attacked = False
