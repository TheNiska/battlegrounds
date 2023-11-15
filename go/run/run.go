package main

import (
    "fmt"
    "example.com/sources"
)

func main() {
    const name = "Denis"

    card1 := sources.NewDefaultCard(3, 7)
    card2 := sources.Card{Attack: 4, Health: 12}
    card1.Do_Attack(&card2)

    fmt.Println(card1)
}
