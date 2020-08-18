#include<iostream>
using namespace std;
int main(){
double arr[6][6]={{1,2,3,4,5,6},{1,2,3,4,5,6},{1,2,3,4,5,6},{1,2,3,4,5,6},{1,2,3,4,5,6},{1,2,3,4,5,6}};
int i=0;
int j=0;
double k=0;
int l=0;
int m=0;
for(i=0;i<6;i++){
    for(m=0;m<6;m++){
        for(j=0;j<6;j++){
            for(l=0;l<6;l++){
                if((arr[i][m]-arr[j][l])>0){
                    if(i>j){
                        k=k+arr[i][m]-arr[j][l]+i-j;
                        }
                    else{
                        k=k+arr[i][m]-arr[j][l]+j-i;
                        }
                    }
                else{
                    if(i>j){
                        k=k-arr[i][m]+arr[j][l]+i-j;
                        }
                    else{
                        k=k-arr[i][m]+arr[j][l]+j-i;
                        }
                    }
                }
            l=0;
            }
        j=0;
        }
    m=0;
    }
double average=(k)/(36*36);
cout<<"The average distance is:"<<average;
return 0;
}
