#include <iostream>
using namespace std;

// bad solution, uses constant big space
int smallestPositiveMissing1(int arr[], int n)
{
    // as n is size of array and we just need to find out minumum missing
    // positive, so need not to take care of elements greater than n+1, because
    // missing number will always be between 1 to n+1, because size of array
    // is n, so only n number can only fit in it
    int occurs[n + 1] = {0};
    for (int i = 0; i < n; i++)
        if (arr[i] > 0 && arr[i] < n + 1)
            occurs[arr[i] - 1] = 1;

    for (int i = 0; i < n + 1; i++)
        if (occurs[i] == 0)
            return i + 1;
}

void swap(int &a, int &b);
int smallestPositiveMissing(int arr[], int n)
{
    // we are using while loop here because, we wont be able to visit that
    // element again, so all swapping shoulb be done until a element arrive which
    // do not satisfy condition
    // arr[arr[i]-1] != arr[i], makes sure we do not fall into infinite loop
    for (int i = 0; i < n; i++)
        while (arr[i] > 0 && arr[i] < n && arr[arr[i] - 1] != arr[i])
            swap(arr[arr[i] - 1], arr[i]);

    for (int i = 0; i < n; i++)
        if (arr[i] != i + 1)
            return i + 1;

    return n + 1;
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

        printf("%d\n", smallestPositiveMissing(arr, n));
    }
    return 0;
}

void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}