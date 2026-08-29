#include<bits/stdc++.h>
using namespace std;

// int main(){
//    int marks;
//    cin>> marks;
//    if (marks < 25){
//     cout<< "F";
//    }
//    if (marks >=25 && marks <=44){
//     cout << "E";
//    }
//    if (marks >= 44 && marks <= 49)
//    {
//        cout << "D";
//    }
//    if (marks >= 50 && marks <= 59)
//    {
//        cout << "c";
//    }
//    if (marks >= 60 && marks <= 79)
//    {
//        cout << "b";
//    }
//    if (marks >= 80 && marks <= 100)
//    {
//        cout << "A";
//    }
// }

// we can writw the above code more efficiently using else if--

int main(){
    int marks;
    cin>>marks;
    if (marks <25){
        cout << "F";

    }
    else if (marks<=44){
        cout<<"D";
    }

    else if(marks<=49){
        cout<< "C";
    }

    else if(marks<=59){
        cout<<"B";

    }

    else if(marks<=79){
        cout<<"A";

    }

    else if(marks<=100){
        cout<<"A+";
    }
}