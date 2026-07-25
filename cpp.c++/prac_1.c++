
#include<iostream>
using namespace std;
int main() {
    /*
    int a = 2;
    int b = a + 1;
    if ((a=3)==b){
        cout<<a;
    }
    else {
        cout<<a+1;
    }
     
    int a = 24;
    if (a>23) {
        cout<<"love";
    }
    else if (a == 24) {
        cout<<"lovely";
    }
    else {
        cout<<"babbar";
    }
    cout<<a;
    //hw
    char ch ;
    cout<<"Enter the value of ch:";
    cin>>ch;
    if (ch>='a'&& ch <= 'z') {
        cout<<"ch is a lower case alphabets";
    }
    else if (ch >='A' && ch <='Z') {
        cout<<"ch is a upper case alphabets";
    }
    else {
        cout<<"ch is a numeric";
    }
        // while
    int a;
    cin>>a;
    int i = 1;
    while (i<=a){
        cout<<i<<" ";
        i +=1;
    }
    
   // sum of all no.
    int a;
    cin>>a;
    int i = 1;
    int count = 0;
    while (i<=a){      // sum = (n/2)(a+l) where a = 1 and l = length 
        count += i;
        i +=1;
    
    }
    cout<<count;
    // sum of all even no.
    int a;
    cin>>a;
    int i = 2;
    int count = 0;
    while (i<=a){
        count += i;
        i += 2;
    }
    cout<<count;
    */

    //prime or not
/* 
    int n ;
    cin>>n;
    int i = 2;
    while (i<n) {
    if (n%i!=0){
        cout<<"prime no. for :"<<i<<endl ;
    }
    else {
        cout << "Not a prime no. for :"<<i<<endl ;
    }
    i +=1;
}}*/

    float c, f;

    cout << "Enter Celsius: ";
    cin >> c;

    f = (c * 9.0/5) + 32;

    cout << "Fahrenheit = " << f<<endl;;

    cout << "Enter Fahrenheit: ";
    cin>>f;

    c = (f-32) *  5.0/9;
    cout<< "Celcius = " << c;

    return 0;
}