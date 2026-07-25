/*#include<iostream>
using namespace std;
int main() {
    int n;
    int i = 1;
    cout<<"Enter the value"<<endl;
    cin>>n;
   while(i<=n) {
    int j = 1 ;
    while(j<=n){
        char ch = 'A'+j-1;
        cout<<ch;                               //output=ABCD
                                                //ABCD
                                                //ABCD
                                                //ABCD
        j++;
    } 
    cout<<endl;
i++;
 }
}
*/



/*#include<iostream>
using namespace std;
int main() {
    int n;
    int i = 1;
    cout<<"Enter the value"<<endl;
    cin>>n;
   char value ='A';
   while(i<=n) {
    int j = 1 ;
    while(j<=n){
        cout<<value;                     //OUTPUT=ABCD
                                         //EFGH
                                         //IJKL
                                         //MNOP
       value=value+1;
        j++;
    } 
    cout<<endl;
i++;
 }
}

*/

/*#include<iostream>
using namespace std;
int main() {
    int n;
    int i = 1;
    cout<<"Enter the value"<<endl;
    cin>>n;
   while(i<=n) {
    int j = 1 ;
    while(j<=n){
        char ch = 'A'+ i+j -2;
        cout<<ch;                                     //OUTPUT=ABCD
                                                      //BCDE
                                                      //CDEF
                                                      //DEFG
       
        j++;
    } 
    cout<<endl;
i++;
 }
}
*/
/*#include<iostream>
using namespace std;
int main() {
    int n;
    int i = 1;
    cout<<"Enter the value"<<endl;
    cin>>n;
   while(i<=n) {
    int j = 1 ;
    while(j<=i){
        char ch = 'A'+ i+j -2;
        cout<<ch;
       
        j++;
    } 
    cout<<endl;
i++;
 }                            //OUTPUT=A
                                     //BC
                                     //CDE
                                     //DEFG
                                     //EFGHI
                        
                    
}

*/

/*#include<iostream>
using namespace std;
int main() {
    int n;
    int i = 1;
    cout<<"Enter the value"<<endl;
    cin>>n;
    char count;
   while(i<=n) {
    int j = 1 ;
     count= 'A'+n-i;
    while(j<=i){
      
        cout<<count;
       count=count+1;
        j++;
    } 
    cout<<endl;
i++;
 }
}//output E
//DE
//CDE
//BCDE
//ABCDE
*/


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
        cout<<count<<" ";
        count = count +1;
        j++;
    } 
    cout<<endl;
i++;
 }
}
