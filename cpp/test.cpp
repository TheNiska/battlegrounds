#include <iostream>

using namespace std;

void print_array(int *arr, int size) {
    for (int i = 0; i < size - 1; i++) {
        cout << *(arr + i) << ", ";
    };
    cout << *(arr + size - 1) << endl;
};

struct Student {
    int num;
    string name;
};

int main() {
    int *p1, *p2;
    int num1 = 100; // 4 bytes
    int num2 = 200;
    int arr[10];
    int arr_length = 10;

    char str[255] = "hello";
    Student student;
    student.num = 10;
    student.name = "denis";

    p1 = &num1;
    p2 = p1 + 1;


    for (int i = 0; i <= 9; i++) {
        *(arr + i) = i;
        cout << arr[i];
    }
    cout << endl;

    print_array(arr, arr_length);

    return 0;
}