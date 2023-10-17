#include <iostream>
#include "base_game.h"

using namespace std;

int main() {
    Card card1(7, 9, false);
    Card card2(3, 9, false);

    card1.do_attack(&card2);

    Game game;
    game.init_board();

    return 0;
}