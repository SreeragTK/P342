#include<iostream>
using namespace std;
int main(){
        double a;
        cout<<"Enter the number upto which you need to sum:";
        cin>>a;
        double b=0;
        double c=1;
        while(c<(a+1)){
                    b=b+c;
                    c++;}
        cout<<"The sum of consecutive integers from 1 to "<<a<<" is "<<b<<"\n";

return 0;
}
