//Name: Alan Q. Shea
//Email: alan.shea65@myhunter.cuny.edu
//Date: December 1, 2020

#include <iostream>
using namespace std;

int main (){
    int credits;
    cout << "Enter number of credits";
    cin >> credits;

    if (credits <= 15){
        cout << "Lower Freshman";
    } else if (credits <= 27){
        cout << "Upper Freshman";
    } else if (credits <= 45){
        cout << "Lower Sophomore";
    } else if (credits <= 60){
        cout << "Upper Sophomore";
    } else if (credits <= 75){
        cout << "Lower Junior";
    } else if (credits <= 93){
        cout << "Upper Junior";
    } else if (credits <= 108){
        cout << "Lower Senior";
    } else {
        cout << "Upper Senior";
    }
    
    cout << '\n';

    return 0;
}