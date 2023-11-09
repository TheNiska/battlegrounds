package main

import (
    "fmt"
    "example.com/sources"
)

func main() {
    const name = "Denis"

    card1 := sources.Card{3, 7}
    card2 := sources.Card{4, 12}
    card1.Do_Attack(&card2)

    fmt.Println(card1, card2)
}
