#include <iostream>
#include <queue>
#include <vector>
#define ll long long
using namespace std;

// brute force - gives tle
ll solver1(ll arr[], int n)
{
    ll out = 0;
    for (int j = 1; j < n; j++)
        for (int i = 0; i < j; i++)
            if (arr[i] <= arr[j] && out < j - i)
                out = j - i;

    return out;
}

// we are checking from ends of the array, it do not reapeat checking of 
// same case, if any case occurs in which condition applies then it must be
// the biggest (j-i)
ll solver(ll arr[], int n)
{
    ll out = 0;
    for (int loop = 1; loop < n; loop++){
        for (int i = 0; i < loop; i++){
            int j = i + (n-loop);
            if(arr[i] <= arr[j])
                return j - i;
        }
    }

    return out;
}

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n;
        cin >> n;
        ll arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        cout << solver(arr, n) << endl;
    }
    return 0;
}
