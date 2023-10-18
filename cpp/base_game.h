#include <iostream>
#include <vector>
#include "base_card.h"
#include <tuple>

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

    tuple<Card*, Card*, bool> next_cards() {
        vector<Card>* brd;
        vector<Card>* opp_brd;
        tuple<Card*, Card*, bool> result;

        if (is_top_move) {
            brd = &top_board;
            opp_brd = &bottom_board;
        } else {
            brd = &bottom_board;
            opp_brd = &top_board;
        };

        bool is_brd_cant_attack = true;
        for (Card card: *brd) {
            if (card.attack > 0) {
                is_brd_cant_attack = false;
                break;
            };
        };

        bool is_opp_brd_cant_attack = true;
        for (Card card: *opp_brd) {
            if (card.attack > 0) {
                is_opp_brd_cant_attack = false;
                break;
            };
        };

        if (is_brd_cant_attack && !is_opp_brd_cant_attack) {
            is_top_move = !is_top_move;
            return next_cards();
        } else if (is_brd_cant_attack && is_opp_brd_cant_attack) {
            return result;
        };

        vector<int> taunts;
        for (int i = 0; i < opp_brd->size(); i++) {
            if (opp_brd->at(i).is_taunt) {
                taunts.push_back(i);
            };
        };

        for (Card card: *brd) {
            if (!card.has_attacked && card.attack > 0) {
                card.has_attacked = true;
                is_top_move = !is_top_move;

                get<0>(result) = &card;
                get<2>(result) = !is_top_move;

                if (taunts.size() < 1) {
                    get<1>(result) = &(opp_brd->at(0));
                } else {
                    get<1>(result) = &(opp_brd->at(taunts[0]));
                };

                return result;
            }
        };

        for (Card card: *brd) {
            card.has_attacked = false;
        };

        return next_cards();

    }
};
