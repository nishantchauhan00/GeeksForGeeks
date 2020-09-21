#include <iostream>
using namespace std;

int helper(int arr[], int n, int i = 0, int val = 0)
{
    if (i == n)
        return val;
    // either you consider a number or not
    return max(helper(arr, n, i + 1, val^arr[i]), helper(arr, n, i + 1, val));
}

int maxSubarrayXOR(int arr[], int n)
{
    return helper(arr, n);
}

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n;
        scanf("%d\n", &n);
        int arr[n];
        for (int i = 0; i < n; i++)
            scanf("%d ", &arr[i]);

        printf("%d\n", maxSubarrayXOR(arr, n));
    }
    return 0;
}
