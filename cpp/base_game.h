#include <iostream>
#include <vector>
#include "base_card.h"

using namespace std;

class Game {
public:
    bool is_top_move = true;
    vector<Card> top_board;
    vector<Card> bottom_board;

    void init_board() {
        Card card1(7, 9, false);
        Card card2(3, 15, false);

        for (int i = 0; i < 7; i++) {
            top_board.push_back(card1);
            bottom_board.push_back(card2);
        };

        cout << "Size: " << top_board.size() << endl;

        for (Card card: top_board) {
            cout << card.get_string() << endl;
        };

    };

};
