/*
# gives tle
def solver1(arr, n, k):
    def helper(sumnow=0, j=0):
        if sumnow == k:
            return 1
        elif sumnow > k:
            return 0
        else:
            out = 0
            for i in range(j, n):
                out += helper(sumnow + arr[i], i + 1)
            return out

    return helper()
*/

/*
The approach for the problem is:

if (A[i] > j)
    DP[i][j] = DP[i-1][j]
else 
    DP[i][j] = DP[i-1][j] OR DP[i-1][sum-A[i]]

> This means that if current element has value greater than ‘current sum value’ 
  we will copy the answer from previous cases
> And if the current sum value is greater than the ‘ith’ element we will see 
  if any of previous states have already experienced the sum=’j’ OR any previous 
  states experienced a value ‘j – A[i]’ which will solve our purpose.
*/
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

long long mod = ((int)pow(10, 9) + 7);

/*
 bottom up DP solution for count of subsets which sum to given sum
 storing count of solutions in dp[i][j] = no. of subsets in arr(0..i-1) that 
 sum to j 
*/
int solver(int n, int arr[], int k)
{
    int dp[n + 1][k + 1] = {0};

    for (int i = 0; i < n + 1; i++)
        dp[i][0] = 1;
    for (int j = 1; j < k + 1; j++)
        dp[0][j] = 0;

    for (int i = 1; i < n + 1; i++)
    {
        for (int j = 1; j < k + 1; j++)
        {
            if (arr[i - 1] > j)
                dp[i][j] = dp[i - 1][j];
            else
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]) % mod;
        }
    }

    return dp[n][k];
}

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        int n, k;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];
        cin >> k;

        cout << solver(n, arr, k) << endl;
    }

    return 0;
}