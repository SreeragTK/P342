#include<iostream>
using namespace std;
int main(){
        double n;
        cout<<"Choose a number of your choice to compute factorial:\n";
        cin>>n;
        double x;
        double m;
        x=n;
        m=n;
        if(n==0){
            cout<<"The value of 0! is 1";
                }
        else if(n>0){
            if(n==1){
                cout<<"The value of 1! is 1";
                    }
            else{
                while(n>1){
                x=x*(n-1);
                n--;
                   }
                cout<<"The value of "<<m<<"! is "<<x;
                 }
               }
        else{
            cout<<"The number you entered is negative!,please enter any positive number(zero included)";
            }
return 0;
}


