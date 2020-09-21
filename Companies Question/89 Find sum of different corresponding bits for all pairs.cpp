#include <iostream>
#define ll long long
#define mod 1000000007
using namespace std;

// gives number of different bits between two numbers
ll diff(ll a, ll b)
{
    ll diff_total = 0;
    while (a || b)
    {
        int x = a & 1, y = b & 1;
        if (x != y)
            ++diff_total;
        a >>= 1;
        b >>= 1;
    }

    return diff_total % mod;
}

// checking each pair once, gives tle
ll solver1(int n, ll arr[])
{
    if (n < 2)
        return 0;

    ll out = 0;
    for (int i = 0; i < n - 1; i++)
        for (int j = i + 1; j < n; j++)
            out += diff(arr[i], arr[j]);

    return (2 * out) % mod;
}

// https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
ll solver(int n, ll arr[])
{
    if (n < 2)
        return 0;

    /*total permutation count will be count*(n-count) and multiply by 2 is due 
    to one more repetition of all this type of pair */
    ll out = 0;
    for (int i = 0; i < 32; i++)
    {
        ll count = 0; // number of bits that are on
        for (int j = 0; j < n; j++)
            if (arr[j] & (1 << i)) // check for i'th bit
                ++count;
        out = (out + count * (n - count)) % mod;
    }

    return (2 * out) % mod;
}

int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int n;
        cin >> n;
        ll arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        cout << solver(n, arr) << endl;
    }

    return 0;
}