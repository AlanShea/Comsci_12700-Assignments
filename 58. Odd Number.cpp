//Name: Alan Q. Shea
//Email: alan.shea65@myhunter.cuny.edu
//Date: December 1, 2020

#include <iostream>
using namespace std;

int main(){
    int number;
    cout << "Please enter an odd number:  ";
    cin >> number;

    while (number % 2 == 0)
    {
        cout << "You entered an even number.\nPlease enter an odd number:  ";
        cin >> number;
    }

    cout << "Your odd number is:  " << number << '\n';
    
    return 0;
}