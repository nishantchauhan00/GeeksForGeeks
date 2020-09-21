#include <stdio.h>

// linear search
int rotatedIndex1(int arr[], int n, int k)
{
    for (int i = 0; i < n; i++)
    {
        if (k == arr[i])
            return i;
    }
    return -1;
}

// linear search on some last part of array and binary search on rest front
// part of it
int rotatedIndex(int arr[], int n, int k)
{
    while (arr[n - 2] < arr[n - 1])
    {
        if (k == arr[n - 1])
            return n - 1;
        n--;
    }
    int l = 0, r = n, mid;

    while (l <= r)
    {
        mid = (r + l) / 2;
        // printf("%d\n", mid);
        if (arr[mid] > k)
            r = mid - 1;
        else if (arr[mid] < k)
            l = mid + 1;
        else
            return mid;
    }

    return -1;
}

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n, k;
        scanf("%d", &n);
        int arr[n];
        for (int i = 0; i < n; i++)
            scanf("%d ", &arr[i]);
        scanf("%d", &k);

        printf("%d\n", rotatedIndex(arr, n, k));
    }
    return 0;
}