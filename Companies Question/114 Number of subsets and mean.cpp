#include <iostream>
#include <unordered_map>
#include <math.h>
#define ll long long
#define mod 1000000007
using namespace std;

/*
https://practice.geeksforgeeks.org/editorial.php?pid=868


Minimum average = minimum value of array
Maximum average = maximum value of array

A min average of a subset from a set is made of only min values of a set and 
max average of a subset from a set is made of only max values of the same set.
*/
void solver(ll arr[], int n)
{
    unordered_map<ll, int> hmap;
    ll min_val = arr[0], max_val = arr[0];
    for (int i = 0; i < n; i++){
        hmap[arr[i]] += 1;
        min_val = min(min_val, arr[i]);
        max_val = max(max_val, arr[i]);
    } 

    // o/p = pow(2, count(min_val)) - 1
    // 1-1   2-3   3-7   4-15
    ll MIN_SUBS = (ll)pow(2, hmap[min_val]) - 1;
    ll MAX_SUBS = (ll)pow(2, hmap[max_val]) - 1;
    printf("%lld %lld\n", MAX_SUBS%mod, MIN_SUBS%mod);
}

int main()
{
    int t;
    scanf("%d\n", &t);
    while (t--)
    {
        int n;
        scanf("%d\n", &n);
        ll arr[n];
        for (int i = 0; i < n; i++)
            scanf("%lld ", &arr[i]);

        solver(arr, n);
    }
    return 0;
}