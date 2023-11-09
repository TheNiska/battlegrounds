package sources 

import "fmt"

type Card struct {
    Attack int
    Health int
}

func (card *Card) Do_Attack(other *Card) {
    card.Health -= other.Attack
    other.Health -= card.Attack
}

func Hello(name string) string {
    // Return a greeting that embeds the name in a message.
    message := fmt.Sprintf("Hi, %v. Welcome!", name)
    return message
}
