// problem link - https://www.codechef.com/SNCKQL21/problems/MAXDISTKT


#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define lld long long double

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define loop(n) for(int i=0;i<n;i++)
#define loop2(n) for(int j=0;j<m;j++)
#define ve vector<ll>
#define pb push_back
#define pob pop_back
#define mpr make_pair
#define mp map<ll, ll>
#define pr pair<ll, ll>
#define all(c) (c).begin(), (c).end()
#define EACH(x, a) for (auto& x: a)

void perform(){
    int number;
    cin>>number;
    pr arrNum[number];
    loop(number){
        cin>>arrNum[i].first;
        arrNum[i].second=i;
    }
    
    sort(arrNum,arrNum+number);
    ve arrNumber(number);
    ll carry = 0;
    loop(number){
        if(carry>=arrNum[i].first && carry!=0)
        arrNumber[arrNum[i].second]=arrNum[i].first;
        
        else
        arrNumber[arrNum[i].second]=(carry++);
    }
    
    loop(number){
        cout<<arrNumber[i]<<" ";
    }
    cout<<"\n";
}


int main() {
  ios::sync_with_stdio(0);
  cin.tie(0); 
  cout.tie(0);
  int tc;
  cin>>tc;
  while(tc--){
      perform();
  }
  return 0;
}
