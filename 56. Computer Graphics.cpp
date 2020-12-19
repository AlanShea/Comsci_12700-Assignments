//Name: Alan Q. Shea
//Email: alan.shea65@myhunter.cuny.edu
//Date: November 24, 2020

#include <iostream>
using namespace std;

void graphic (int length){
    for (int i = 0; i < length; i++){
        cout << "* ";
    }
    cout << "\n";
    if (length > 0){
        graphic (length - 1);
    }
}

int main (){
    int x;
    cout << "Please enter a number:  ";
    cin >> x;
    cout << "\n";
    graphic (x);

    return 0;
}