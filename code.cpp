#include<bits/stdc++.h>
using namespace std;

void doSomething(int arr[], int n){
    arr[0]+=100;
    cout<<"value inside func:"<<arr[0]<<endl;
}
void printPattern(int n){
    for (int i=0; i<n;i++){
        for(int j=0;j<=i;j++){
            cout<< " ";
        }
        for (int j=0 ;j < 2*n - (2*i + 1);j++){
            cout<<"*";
        }
        for (int j = 0; j <=i; j++)
        {
            cout << " ";
        }

        cout<<endl;
    }

}
int main(){
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        int n;
        cin>>n;
        printPattern(n);
    }

return 0;
}
