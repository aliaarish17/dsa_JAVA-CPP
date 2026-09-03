#include<bits/stdc++.h>
using namespace std;

void doSomething(int arr[], int n){
    arr[0]+=100;
    cout<<"value inside func:"<<arr[0]<<endl;
}
void printPattern(int n){
    for (int i = 1; i <= 2 * n - 1; i++) {
        // Kitne stars print karne hain, uska calculation:
        int stars = i;
        if (i > n) {
            stars = 2 * n - i;
        }

        // Stars print karne ka loop
        for (int j = 1; j <= stars; j++) {
            cout << "*";
        }
        cout << endl;
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
