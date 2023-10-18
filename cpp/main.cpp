#include <iostream>
#include "base_game.h"

using namespace std;

int main() {
    Card card1(7, 9, false);
    Card card2(3, 9, false);

    card1.do_attack(&card2);

    Game game;
    game.init_board();
    tuple<Card*, Card*, bool> result = game.next_cards();
    cout << (get<0>(result))->get_string() << endl;

    return 0;
}