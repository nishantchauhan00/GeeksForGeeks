#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    //
    //
    // RECURSION //////////////////////////////////////////
    bool helper1(int i, int left, int arr[], int n)
    {
        if (left == 0)
            return true;
        if (i == n)
            return false;

        return helper1(i + 1, left, arr, n) or helper1(i + 1, left - arr[i], arr, n);
    }

    int equalPartition1(int N, int arr[])
    {
        int total = 0;
        total = accumulate(arr, arr + N, total);

        if (total % 2 != 0)
            return 0;
        else
            return helper1(0, total / 2, arr, N);
    }
    /////////////////////////////////////////////////
    //
    //
    /////////////////////////////////////////////////
    // DP ///////////////////////////////////////////
    /////////////////////////////////////////////////
    int helper(int i, int left, int arr[], int n, int **dp)
    {
        if (left == 0)
            return 1;
        if (i == n or left < 0)
            return 0;
        if (dp[i][left] != -1)
            return dp[i][left];

        dp[i][left] = helper(i + 1, left, arr, n, dp) + helper(i + 1, left - arr[i], arr, n, dp);
        return dp[i][left];
    }

    int equalPartition(int n, int arr[])
    {
        int total = 0;
        total = accumulate(arr, arr + n, total);

        if (total % 2 != 0)
            return 0;
        else
        {
            int **dp;
            int half = total / 2;
            dp = new int *[n + 1];
            for (int i = 0; i < n + 1; i++)
                dp[i] = new int[half + 1];
            for (int i = 0; i < n + 1; i++)
                for (int j = 0; j < half + 1; j++)
                    dp[i][j] = -1;
            return helper(0, half, arr, n, dp);
        }
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin >> N;
        int arr[N];
        for (int i = 0; i < N; i++)
            cin >> arr[i];

        Solution ob;
        if (ob.equalPartition(N, arr))
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    return 0;
}