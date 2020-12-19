//Name: Alan Q. Shea
//Email: alan.shea65@myhunter.cuny.edu
//Date: December 1, 2020

#include <iostream>
using namespace std;

int main(){
    int year = 0;
    float startAmount;
    cout << "Please enter the starting amount:  ";
    cin >> startAmount;
    float stepAmount = startAmount;
    float limit = startAmount + 1000;
    while (stepAmount < limit){
        stepAmount = stepAmount * 1.03;
        year++;
        cout << "Year " << year << "   " << stepAmount << '\n';
    }
    
    return 0;
}