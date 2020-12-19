//Name: Alan Q. Shea
//Email: alan.shea65@myhunter.cuny.edu
//Date: November 24, 2020

#include <iostream>
using namespace std;

int main () {
    float c;
    cout << "Enter degrees in celsius:  ";
    cin >> c;

    float f = c / 5.0 * 9.0 + 32;
    cout << "\n The degrees in farenheit is:  " << f << "\n";

    return 0;
}    