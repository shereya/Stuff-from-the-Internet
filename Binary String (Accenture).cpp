#include<iostream>
#include<map>
#include<string>
using namespace std;
int main()
{
    map<string,string>operation;
    int result;
    //and operation 
    operation["0A0"]="0";
    operation["0A1"]="0";
    operation["1A0"]="0";
    operation["1A1"]="1";
    //or operator
    operation["0B0"]="0";
    operation["0B1"]="1";
    operation["1B0"]="1";
    operation["1B1"]="1";
    //xor operator 
    operation["0C0"]="1";
    operation["0C1"]="0";
    operation["1C0"]="0";
    operation["1C1"]="1";
    string s="1C0C1C1A0B1";
    string res;
    string s1;
    for(int i=0;i<3;i++)
    {
        res=res+s[i];
    }
    res=operation[res];
    for(int i=3;i<s.length();i=i+2)
    {
        s1=res+s[i]+s[i+1];
        res=operation[s1];
    }
    result=stoi(res);
    cout<<result<<endl;
}
