//zoho count heads question
#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main()
{
    int n=4;
    int k=3;
    vector<string>v={"H","T"};
    for(int i=1;i<n;i++)
    {
        vector<string>temp;
        for(int j=0;j<v.size();j++)
        {
            temp.push_back(v[j]+"H");
        }
        for(int j=0;j<v.size();j++)
        {
            temp.push_back(v[j]+"T");
        }
        v=temp;
    }
    int prob=0;
    for(int i=0;i<v.size();i++)
    {
        string s=v[i];
        int count = 0;
        for(int j=0;j<s.size();j++)
        {
            if(s[j]=='H')
            {
                count++;
            }
        }
        if(count==k)
        {
            prob++;
        }
    }
    cout<<static_cast<double>(prob)/v.size() << endl;
}
