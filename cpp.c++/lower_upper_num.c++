#include<iostream>
using namespace std;
int main() {
    char ch;
    cout<<"Enter a character"<<endl;
    cin>> ch;
    if(ch>='a' && ch<='z') {
        cout<<"lower case alphabets"<<endl;
    }    
    else if(ch>='A' && ch<='Z'){
        cout<<"Upper case alphabets"<<endl;
    }
    else if(ch>='0' && ch<='9') {
        cout<<"numbers"<<endl;
    }
    else {
        cout<<"Special character"<<endl;
    }
}







int main() {
    int ans = 0;
    int i = 0;
    int n ;
    cin >> n;
    while(n > 0){
        int bit = n & 1;
        ans = (bit * pow(10,i)) + ans;
        n = n >> 1;
        i++;
        cout << i <<" ";
        cout<< bit;
    }
    cout<< ans <<endl;
}
