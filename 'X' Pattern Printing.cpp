//x-pattern printing - zoho 
//TC-O(n^2)
//SC-O(n^2)
#include<iostream>
#include<string>
using namespace std;
int main()
{
    string str;
    cin>>str;
    char mat[100][100];
    int e=0;
    for(int i=0;i<str.length();i++)
    {
        for(int j=0;j<str.length();j++)
        {
            if(i==j)
            {
                mat[i][j]=str[e];
                e++;
            }
            else
            {
                mat[i][j]=' ';
            }
        }
    }
    e=str.length()-1;
    for(int i=0;i<str.length();i++)
    {
        for(int j=0;j<str.length();j++)
        {
            if(i+j==str.length()-1)
            {
                mat[i][j]=str[e];
                e--;
            }
        }
    }
    for(int i=0;i<str.length();i++)
    {
        for(int j=0;j<str.length();j++)
        {
            cout<<mat[i][j];
        }
        cout<<endl;
    }
}
