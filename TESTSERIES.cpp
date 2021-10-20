// problem link - https://www.codechef.com/SNCKQL21/problems/TESTSERIES

#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
#define int long long int
#define pb push_back
using namespace std;
using namespace __gnu_pbds;
#define N 1000000007
#define PI 3.141592653589793238462
signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int testcase;
    cin >> testcase;
    while(testcase--)
    {
        vector<int> v(5);
        int ind = 0, eng = 0, draw = 0;
        for(int i=0; i<5; i++)
        {
            cin >> v[i];
        }
        for(int i=0; i<5; i++)
        {
            if(v[i]==1){
                ind++;
            }
            if(v[i]==0){
                draw++;
            }
            if(v[i]==2)
            {
                eng++;
            }
        }
        if(ind > eng){
            cout <<"INDIA" << endl;
        }
        else if(eng > ind){
            cout << "ENGLAND" << endl;
        }
        else{
            cout << "DRAW" << endl;
        }
    }
    return 0;
}
