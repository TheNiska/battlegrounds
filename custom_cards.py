from models.base_card import Card
from models.pygame_card import PyGameCard

is_pygame = True
inherited_class = PyGameCard if is_pygame else Card


class Annoy_o_Tron(inherited_class):
    def __init__(self):
        super().__init__(attack=1, health=2)
        self.name = 'Annoy-o-Tron'
        self.is_bubbled = True
        self.is_taunt = True


class Dozy_Whelp(inherited_class):
    def __init__(self):
        super().__init__(attack=0, health=3)
        self.name = 'Dozy Whelp'
        self.is_taunt = True

    def before_attacked(self, other):
        self.attack += 1
        self.can_attack = True  # need to do it if default attack is 0


class Micro_Mummy(inherited_class):
    def __init__(self):
        super().__init__(attack=1, health=2)
        self.name = 'Micro Mummy'
        self.is_reborn = True


if __name__ == "__main__":
    def_classes = [Card, PyGameCard, inherited_class]
    global_objs = list(globals().items())

    for name, obj in global_objs:
        if obj not in def_classes and isinstance(obj, type):
            card = obj()
            print(card.name)
