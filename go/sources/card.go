package sources 

import (
    "math/rand"
)

type Card struct {
    Attack int
    Health int
    Name string

    Is_bubbled bool
    Is_poison bool
    Is_reborn bool
    Is_taunt bool

    is_dead bool
    has_lost_hp bool
    has_attacked bool
}

func NewDefaultCard(atk int, hlth int) *Card {
    card := Card{Attack: atk, Health: hlth}
    card.Name = "Default_Card"

    // if rand generates 1 then value is true
    poison := rand.Intn(10)
    bubble := rand.Intn(7)
    reborn := rand.Intn(7)
    taunt := rand.Intn(7)

    if poison == 1 { card.Is_poison = true}
    if bubble == 1 { card.Is_bubbled = true}
    if reborn == 1 { card.Is_reborn = true}
    if taunt == 1 { card.Is_taunt = true}

    return &card
}

func (card *Card) Before_Attacked(other *Card) {}
func (card *Card) Before_Attack(other *Card) {}

func (card *Card) Takes_Damage(other *Card) {
    if card.Is_bubbled {
        card.Is_bubbled = false
        return
    }

    if other.Is_poison {
        card.Health = 0
        card.has_lost_hp = true
        return
    }

    card.Health -= other.Attack
    card.has_lost_hp = true
}

func (card *Card) Do_Attack(other *Card) {
    card.Before_Attack(other)
    other.Before_Attacked(card)

    other.Takes_Damage(card)
    card.Takes_Damage(other)
}

