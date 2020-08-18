#include<iostream>
using namespace std;
int main(){
int a[]={1,3,6};
int i=0;
//printing vector A
cout<<"The vector A is:"<<"[";
    for(i=0;i<3;i++){
            if(i==2){
                cout<<a[i];
            }
            else{
                cout<<a[i]<<",";
            }
    }
    cout<<"]\n";
int b[]={2,7,9};
i=0;
cout<<"The vector B is:"<<"[";
    for(i=0;i<3;i++){
            if(i==2){
                cout<<b[i];
            }
            else{
                cout<<b[i]<<",";
            }
    }
    cout<<"]\n";
//computing sum and dot product
int Sum[]={0,0,0};
int dot_product=0;
i=0;
for(i=0;i<3;i++){
    Sum[i]=a[i]+b[i];
    }
cout<<"The sum of these two vectors is(A+B):[";
for(i=0;i<3;i++){
        cout<<Sum[i]<<",";
    }
cout<<"]\n";
i=0;
while (i<3){
    dot_product=dot_product+(a[i]*b[i]);
    i+=1;
    }
cout<<"The dot product of these two vectors is(A.B):"<<dot_product;
//The output is:
//The vector B is:[1,3,6]
//The vector B is:[2,7,9]
//The sum of these two vectors is(A+B):[3,10,15]
//Dot product of these two vectors is(A.B):77
return 0;
}
