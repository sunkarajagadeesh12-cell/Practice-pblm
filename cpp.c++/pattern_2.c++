/* 
#include<iostream>
using namespace std;
int main() {
    int n;
    int i = 1;
    cout<<"Enter the value"<<endl;
    cin>>n;
    int count = 1;
   while(i<=n) {
    int j = 1 ;
    while(j<=i){
        cout<<count;
        count = count + 1;
        j++;
    } 
    cout<<endl;
i++;
 }
}
 

#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int i = 1;
    while (i<=n){
        int space = i-1;
        while(space>0){
            cout<<" ";
            space -= 1;
        }
        int j = 1;
        int start = n-i+1;
        int value = i;
        while (j<=start) {
            cout<<value;
            value += 1;
            j =j+1;
        }
        cout<<endl;
        i=i+1;
    }
}  

#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int i = 1;
    int count = 1;
    while (i<=n){
        int space = n-i;
        while(space>0){
            cout<<" ";
            space -= 1;
        }
        int j = 1;
        while (j<=i) {
            cout<<count<<" ";
            count += 1;
            j =j+1;
        }
        cout<<endl;
        i=i+1;
    }
} */

/*
#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int i = 1;
    while (i<=n){
        int space = n-i;
        while(space>0){
            cout<<" ";
            space -= 1;
        }
        int j = 1;
        while (j<=i) {
            cout<<j;
            j =j+1;
        }
        int start = i-1;
        while (start>0){
            cout<<start;
            j =j+1;
            start -=1;
        }
        cout<<endl;
        i=i+1;
    }
} */


#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int i = 1;
    int count = n;
    while (i<=n){
        // first triangle
        int start = n-i+1;
        int j = 1;
        while (j<=start) {
            cout<<j;
            j = j + 1;
        }
        //second triangle
        int star = i-1;
        while (star){
            cout<<'*';
            star = star - 1;
        }
        // third triangle
        int star1 = i-1;
        while (star1) {
            cout<<'*';
            star1 -= 1;
        }
        //fourth triangle
        
        int start1 = n-i+1;   
        int k = 1;
        while (k<=start1) {
            cout<<start1-k+1;
            k += 1;
        }
        cout<<endl;
        i=i+1;
    }
} 
