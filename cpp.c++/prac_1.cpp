#include<bits/stdc++.h>
using namespace std;

int main(){

    string s="aba";

            string p =s+s;
        string ans=p.substr(1,(2*s.length())-2);
        auto i=find(ans.begin(),ans.end(),"aba");        
        if(i!=ans.end()){
            cout<<false<<endl;
        }
        cout<<true<<endl;

    return 0;
}