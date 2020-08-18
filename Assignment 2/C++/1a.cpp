#include<iostream>
using namespace std;
int main(){
double arr[]={1,2,3,4,5,6};
int i=0;
int j=0;
double k=0;
double average;
for (i=0;i<6;i++){
    for (j=0;j<6;j++){
        if((arr[j]-arr[i])>0){
            k=k+arr[j]-arr[i];
            }
        else{
            k=k+arr[i]-arr[j];
            }
        }
    j=0;
    }
average=(k/36);
cout<<"The average distance is:"<<average;
//The output is:
//The average distance is 1.94444
return 0;
}
