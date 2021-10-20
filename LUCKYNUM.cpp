// problem link - https://www.codechef.com/SNCKQL21/problems/LUCKYNUM

#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
#define int long long int
#define pb push_back
using namespace std;
using namespace __gnu_pbds;
#define N 1000000007
#define PI 3.141592653589793238462
signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int testcase;
    cin >> testcase;
    while(testcase--)
    {
        int num1, num2, num3;
        cin >> num1 >> num2 >> num3;
        if(num1 == 7 || num2 == 7 || num3 == 7)
        {
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }
    return 0;
}
