#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
using namespace std;
int main(){
    //reading matrix M from the .txt file m
    ifstream file_m;
    file_m.open("m.txt");
    double M[3][3];
    int i=0;
    int j=0;
    double x;
    string line;
    for(i=0;getline(file_m, line);i++){
            istringstream stream(line);
            for(j=0;stream>>x;j++){
                M[i][j]=x;
            }
        }
    i=0;
    j=0;
    //printing of Matrix "M"
    cout<<"Matrix M is: [";
    for(i=0;i<3;i++){
        cout<<"[";
        for(j=0;j<3;j++){
            if(j==2){
                cout<<M[i][j];
                }
            else{
                cout<<M[i][j]<<",";
                }
            }
        cout<<"]";
        j=0;
        }
    cout<<"]\n";
    i=0;
    j=0;
    //reading Matrix N from the .txt file n
    ifstream file_n;
    file_n.open("n.txt");
    double N[3][3];
    double y;
    for(i=0;getline(file_n, line);i++){
            istringstream stream(line);
            for(j=0;stream>>y;j++){
                N[i][j]=y;
            }
        }
    //printing matrix "N"
    cout<<"Matrix N is: [";
    for(i=0;i<3;i++){
        cout<<"[";
        for(j=0;j<3;j++){
            if(j==2){
                cout<<N[i][j];
            }
            else{
                cout<<N[i][j]<<",";
            }
        }
        cout<<"]";
        j=0;
        }
    cout<<"]\n";
    //printing matrix "A"
    double a[]={1,3,6};
    cout<<"Matrix A is:"<<"[";
    for(i=0;i<3;i++){
            if(i==2){
                cout<<a[i];
            }
            else{
                cout<<a[i]<<",";
            }
    }
    cout<<"]\n";
    i=0;
    j=0;
    double k[]={0,0,0};
    //calculation of M x A
    while(i<3){
        while(j<3){
            k[i]=k[i]+((M[i][j])*a[j]);
            j++;
            }
        j=0;
        i++;
        }
    //printing "M x A"
    cout<<"M x A is:"<<"[";
    for(i=0;i<3;i++){
            if(i==2){
                cout<<k[i];
            }
            else{
                cout<<k[i]<<",";
            }
    }
    cout<<"]\n";
    //computing M x N
    double l[3][3]={{0,0,0},{0,0,0},{0,0,0}};
    i=0;
    j=0;
    int s=0;
    int g=0;
    int h=0;
    while(h<3 and g<3){
        while(i<3 and s<3){
            while(j<3){
                l[g][s]=l[g][s]+(int(M[h][j])*int(N[j][i]));
                j+=1;
                }
            j=0;
            i+=1;
            s+=1;
            }
        i=0;
        s=0;
        h+=1;
        g+=1;
        }
    i=0;
    j=0;
    //printing M x N
    cout<<"Matrix M x N is: [";
    for(i=0;i<3;i++){
        cout<<"[";
        for(j=0;j<3;j++){
            if(j==2){
                cout<<l[i][j]<<",";
                }
            else{
                cout<<l[i][j]<<",";
                }
            }
        cout<<"]";
        j=0;
        }
    cout<<"]\n";
return 0;
}
