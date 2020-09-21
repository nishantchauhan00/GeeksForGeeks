/*
> k and n are always positive
> array integers can be +ve or -ve

You are given an array A of N positive and/or negative integers and a value K. 
The task is to find the count of all sub-arrays whose sum is divisible by K.
*/

#include <iostream>
using namespace std;

int solver(int arr[], int n, int k)
{
    int count = 0, sum_arr = 0;
    int dp[k] = {0};
    // we are initializing it with 0 because even on first occurence we have 
    // to add it to count as it is clear divisible by k
    dp[0] = 1; 

    for (int i = 0; i < n; i++)
    {
        sum_arr += arr[i];
        count += dp[sum_arr % k];
        dp[sum_arr % k] += 1;
    }

    return count;
}

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n, k;
        scanf("%d %d\n", &n, &k);
        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        printf("%d\n", solver(arr, n, k));
    }
    return 0;
}
