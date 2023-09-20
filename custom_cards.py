from models import Card


class Annoy_o_Tron(Card):
    def __init__(self):
        super().__init__(attack=1, health=2)
        self.is_bubbled = True
        self.is_taunt = True


class Dozy_Whelp(Card):
    def __init__(self):
        super().__init__(attack=0, health=3)
        self.is_taunt = True

    def before_attacked(self, other):
        self.attack += 1
        self.can_attack = True  # need to do it if default attack is 0


class Micro_Mummy(Card):
    def __init__(self):
        super().__init__(attack=1, health=2)
        self.is_reborn = True
