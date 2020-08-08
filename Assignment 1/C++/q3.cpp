#include<iostream>
using namespace std;
int main(){
        double a=1;
        double b=0;
        while((1/a)>.001){
                    b=b+(1/a);
                    a++;
                    }
        cout<<"The sum is "<<b;

return 0;
}
