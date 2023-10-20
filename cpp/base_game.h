#include <iostream>
#include <vector>
#include "base_card.h"
#include <tuple>

using namespace std;

void delete_element(Card *arr, int *len, int index) {
    for (int i = index; i < *len - 1; i++) {
        *(arr + i) = *(arr + i + 1);
    };
    (*len)--;
};


class Game {
public:
    bool is_top_move = true;
    Card top_board[7];
    Card bottom_board[7];
    int top_len = 7;
    int btm_len = 7;
    

    void print_boards() {
        for (int i = 0; i < top_len; i++) {
            cout << (*(top_board + i)).get_string() << "  ";
        };
        cout << endl;
        for (int i = 0; i < btm_len; i++) {
            cout << (*(bottom_board + i)).get_string() << "  ";
        };
        cout << endl;
    };

    /*
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

                cout << card.get_string();
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
    */
};
