#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>> n;
    int temp = n;
    int sum =0;
    while(n>0){
        int ld= n%10  ;
        sum = sum+ (ld*ld*ld);
        n=n/10;
    }
    if(temp == sum) {
        cout<< "yes"<< sum;
    }
    else {
        cout<< "no";
    };
}