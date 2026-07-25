#include<iostream>
using namespace std;
int main() {
    /*
    int sum=0;
    int i=1;
    int n;
    cout<<"Enter the value"<<endl;
    cin>>n;
    while(i<=n) {
        sum=sum+i;
    i=i+2;
    }
    cout<<"sum of the value is "<<sum<<endl;
}

// for loop
    int n;
    cout << "Enter the value of n:" << endl;
    cin >> n;
    cout <<"Printing count from 1 to n" << endl;
    int i = 1;
    for(; ; ){
        if(i<=n) {
            cout << i << endl;
        }
        else{
            break;
        }
        i++;
    }
}
// for loop-2
    int n;
    cout <<"Enter the value of n:" << endl;
    cin >> n;
    int sum = 0;
    for(int i= 1;i<= n;i++){
        sum += i;
    }
    cout << "Sum of all element is :- " << sum << endl;
}

    int n = 10;

    int a = 0;
    int b = 1;

    cout << a << " " << b << " ";
    for(int i = 1;i <=n;i++){
        int sum = a+b;
        cout << sum << " ";
        a = b;
        b = sum;
    }
}

    int n;
    cout << "Enter the value of n:" << endl;
    cin>> n;
    bool isprime = 1;
    for(int i = 2;i<n;i++){
        if(n%i==0){
            //cout << "It is not a prime number"<<endl;
            isprime = 0;
            break;
        }
    }
        
    if(isprime == 0){
        cout << "It is not a prime number"<<endl;
        }
    else{
        cout << "It is a prime number"<<endl;
        }

    

// continue
int n =5;
    for(int i=0; i<n ; i++){
        cout<< " HEY " << endl;
        cout<< " Hello " << endl;
        continue;
        cout<< " HY " << endl;
    }
}
}*/
/*
//question1:-
    for(int i=0; i<=5 ; i++){
        cout<< i << " ";
        i++;
    }
}
*/
//question2:-
/*
    for(int i=0 ; i<=5 ; i--){
        cout<< i << " ";
        i++;
    }
}
*/
//question3:- doubt
/*
    for(int i=0; i<=15; i+=2){
        cout<< i << " ";
        if(i&1) {
            continue;
        }
        i++;
    }
}*/

//question4:-

    for(int i=0; i<5; i++){
        for(int j=1; j<=5; j++){
            cout<< i << " " << j << endl;
        }
    }
}