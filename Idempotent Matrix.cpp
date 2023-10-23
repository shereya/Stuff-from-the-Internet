//idempotent matrix 
#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int n=3;
    int mat[n][n];
    int res[n][n];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cin>>mat[i][j];
        }
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            res[i][j]=0;
            for(int k=0;k<n;k++)
            {
                res[i][j]=res[i][j]+(mat[i][k]*mat[k][j]);
            }
        }
    }
    int flag=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(mat[i][j]!=res[i][j])
            {
                flag=-1;
            }
        }
    }
    if(flag==0)
    {
        cout<<"true"<<endl;
    }
    else
    {
        cout<<"false"<<endl;
    }
}
