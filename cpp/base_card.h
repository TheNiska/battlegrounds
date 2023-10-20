#ifndef BASE_CARD_H
#define BASE_CARD_H

#include <iostream>

using namespace std;

class Card {
public:
    int attack;
    int health;
    bool is_bubbled = false;

    bool has_lost_hp = false;
    bool is_poison = false;
    bool is_reborn = false;
    bool is_taunt = false;
    bool is_dead = false;
    bool has_attacked = false;

    Card(int attack_arg, int health_arg, bool is_bubbled_arg) {
        attack = attack_arg;
        health = health_arg;
        is_bubbled = is_bubbled_arg;
    };

    Card() {
        attack = 0;
        health = 0;
    };

    string get_string() {
        string atk_info = to_string(attack);
        if (is_poison) {
            atk_info += "p";
        };

        string health_info = to_string(health);
        if (is_bubbled) {
            health_info += "b";
        };
        if (is_reborn) {
            health_info += "r";
        };
        if (is_taunt) {
            health_info += "t";
        };

        string result;
        result = "(" + atk_info + " | " + health_info + ")";
        return result;

    }

    void before_attack(Card* other) {};

    void before_attacked(Card* other) {};

    void takes_damage(Card* other) {
        if (is_bubbled) {
            is_bubbled = false;
            return;
        };

        if (other->is_poison) {
            health = 0;
            has_lost_hp = true;
        };

        health -= other->attack;
        has_lost_hp = true;
    };

    void do_attack(Card* other) {
        before_attack(other);
        other->before_attacked(this);

        other->takes_damage(this);
        takes_damage(other);
    };

    void die() {
        is_dead = true;
    };

    void print() {
        cout << "( " << attack << ", " << health << " )\n";
    };

};

#endif