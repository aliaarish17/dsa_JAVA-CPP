#include<bits/stdc++.h>
using namespace std;

int main(){
   int marks;
   cin>> marks;
   if (marks < 25){
    cout<< "F";
   }
   if (marks >=25 && marks <=44){
    cout << "E";
   }
   if (marks >= 44 && marks <= 49)
   {
       cout << "D";
   }
   if (marks >= 50 && marks <= 59)
   {
       cout << "c";
   }
   if (marks >= 60 && marks <= 79)
   {
       cout << "b";
   }
   if (marks >= 80 && marks <= 100)
   {
       cout << "A";
   }
}