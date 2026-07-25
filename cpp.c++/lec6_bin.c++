// Binary to Decimal

#include<bits/stdc++.h>
using namespace std;

/*
int main() {
    int n;
    cin>> n;
    int ans=0 , i=0 ;
    while(n!=0){
        int digit = n%10;
        if(digit == 1){
            ans = pow(2,i) + ans;
        }
        n = n/10;
        i++;
    }
    cout<< "The Decimal is :"<< ans <<endl;
}



int main() {
    int ans = 0;
    int i = 0;
    int n , j;
    cin >> n;
    while(n > 0){
       int bit = n%2==0 ? 0 : 1;
       j = ceil(pow(10,i));
       int h = bit *j;
        ans = h + ans;
        n = n >> 1;
        cout << i <<" "<< bit << " " << ans <<endl;
        i++;
    }
    cout<< ans <<endl;
}
*/



#include <iostream>
#include <cmath> // Required for pow() and round()
using namespace std;

int main() {
    int num;
    cout << "Enter an integer: ";
    cin >> num;

    int originalNum = num;
    int sum = 0;
    int digits = 0;

    // Step 1: Count the number of digits
    int temp = num;
    while (temp > 0) {
        temp = temp / 10;
        digits++;
    }

    // Step 2: Extract each digit and use pow()
    temp = num; // Reset temp back to the original number
    while (temp > 0) {
        int lastDigit = temp % 10; // Grab the right-most digit
        
        // Calculate (lastDigit ^ digits) and round it safely!
        int powerResult = round(pow(lastDigit, digits)); 
        
        sum += powerResult; // Add it to our running total
        temp = temp / 10;   // Remove the right-most digit
    }

    // Step 3: Check if it matches
    if (sum == originalNum) {
        cout << originalNum << " is an Armstrong number." << endl;
    } else {
        cout << originalNum << " is NOT an Armstrong number." << endl;
    }

    return 0;
}

