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
    while(j<=n){
        cout<<count;
        count = count +1;
        j++;
    } 
    cout<<endl;
i++;
 }
}*/

/*
#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int i = 1;
    while (i<=n){
        int j = 1;
        while (j<=n){
            cout<<'*';
            j =j + 1;
        }
        cout<<endl;
        i=i+1;
    }
}*/

/* 
#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int i = 1;
    while (i<=n){
        int j = 1;
        while (j<=n){
            cout<<j;
            j =j + 1;
        }
        cout<<endl;
        i=i+1;
    }
}
*/

/* 
#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int i = 1;
    while (i<=n){
        int j = 1;
        while (j<=n){
            cout<<i;
            j =j + 1;
        }
        cout<<endl;
        i=i+1;
    }
}
*/

/*
#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int i = 1;
    while (i<=n){
        int j = 1;
        while (j<=n){
            cout<<n-j+1;
            j =j+1;
        }
        cout<<endl;
        i=i+1;
    }
}
*/

/* 
#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int i = 1;
    int count=1;
    while (i<=n){
        int j = 1;
        while (j<=n){
            cout<<count<< " ";
            count +=1;
            j =j+1;
        }
        cout<<endl;
        i=i+1;
    }
}
*/

/* 
#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int i = 1;
    while (i<=n){
        int j = 1;
        while (j<=i){
            cout<<'*';
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
    while (i<=n){
        int j = 1;
        while (j<=i){
            cout<<i;
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
    int count = 1;
    int i = 1;
    while (i<=n){
        int j = 1;
        while (j<=i){
            cout<<count<<" ";
            count+=1;
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
    while (i<=n){
        int j = 1;
        int value = i;
        while (j<=i){
            cout<<value<<" ";
            value -=1;
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
    while (i<=n){
        int j = 1;
        int value = i;
        while (j<=i){
            cout<<value<<" ";
            value +=1;
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
    while (i<=n){
        int j = 1;
        while (j<=n){
            char ch ='A'+i-1; 
            cout<<ch<<" ";
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
    while (i<=n){
        int j = 1;
        while (j<=n){
            char ch ='A'+j-1; 
            cout<<ch<<" ";
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
        int j = 1;
        while (j<=n){
            char ch ='A'+count-1; 
            count += 1;
            cout<<ch<<" ";
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
    while (i<=n){
        int j = 0;
        while (j<=n-1){
            char ch ='A'+i+j-1; 
            cout<<ch<<" ";
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
    while (i<=n){
        int j = 1;
        while (j<=i){
            char ch ='A'+i-1; 
            cout<<ch<<" ";
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
    int i = 1;\
    int count = 1;
    while (i<=n){
        int j = 1;
        while (j<=i){
            char ch ='A'+count-1;
            count += 1; 
            cout<<ch<<" ";
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
    while (i<=n){
        int j = 1;
        int value = i;
        while (j<=i){
            char ch ='A'+value-1;
            value += 1; 
            cout<<ch<<" ";
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
    while (i<=n){
        int j = 1;
        char start = 'A'+n-i;
        while (j<=i){
            cout<<start<<" ";
            start += 1;
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
    while (i<=n){
        int j = 1;
        int value = i;
        while (j<=n){
            char ch = 'A'+value-1;
            cout<<ch<<" ";
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
    while (i<=n){
        int space = n-i;
        while(space>0){
            cout<<" ";
            space -= 1;
        }
        int j = 1;
        while (j<=i) {
            cout<<'*';
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
    while (i<=n){
        int j = 1;
        int start = n-i+1;
        while (j<=start){
            cout<<'*';
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
    while (i<=n){
        int space = i-1;
        while(space>0){
            cout<<" ";
            space -= 1;
        }
        int j = 1;
        int start = n-i+1;
        while (j<=start) {
            cout<<'*';
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
    while (i<=n){
        int space = i-1;
        while(space>0){
            cout<<" ";
            space -= 1;
        }
        int j = 1;
        int start = n-i+1;
        while (j<=start) {
            cout<<i;
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
    while (i<=n){
        int space = n-i;
        while(space>0){
            cout<<" ";
            space -= 1;
        }
        int j = 1;
        while (j<=i) {
            cout<<i;
            j =j+1;
        }
        cout<<endl;
        i=i+1;
    }
}
*/