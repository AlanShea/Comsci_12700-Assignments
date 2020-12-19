//Name: Alan Q. Shea
//Email: alan.shea65@myhunter.cuny.edu
//Date: December 1, 2020

#include <iostream>
using namespace std;

int main(){
    int x;
    int n;
    int b = 16;

    cout << "Enter a number:  ";
    cin >> n;

    if (n < 0){
        cout << 1;
        x = 32 + n;
    } else {
        cout << 0;
        x = n;
    }

    while (b > 0.5)
    {
        if (x >= b)
        {
            cout << 1;
        } else {
            cout << 0;
        }
        x = x % b;
        b = b / 2;
    }
    
    cout << '\n';

    return 0;
}