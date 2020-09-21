#include <iostream>
#include <vector>
#include <cmath>
#define ll long long
using namespace std;

ll mod = ((int)pow(10, 9) + 7);

int solver1(int n, int i = 0, bool prev = false)
{
    if (i == n)
        return 1;

    // if previous bit was on, then cannot considering current bit
    if (prev)
        return solver1(n, i + 1, false)%mod;
    else // if previous bit was off, then we can consider current bit
        return (solver1(n, i + 1, false) + solver1(n, i + 1, true))%mod;
}

int solver(int n){
    if (n <= 2)
        return n + 1;
        
    ll dp[n+1] = {0, 2, 3};
    
    for(int i = 3; i<n+1; i++)
        dp[i] = (dp[i-1] + dp[i-2])%mod;
    
    return dp[n];
}

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        int n;
        cin >> n;
        cout << solver(n) << endl;
    }
    return 0;
}