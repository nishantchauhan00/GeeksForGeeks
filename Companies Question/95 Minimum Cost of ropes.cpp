#include <iostream>
#include <queue>
#include <vector>
#define ll long long
using namespace std;

ll solver(ll arr[], int n)
{
    priority_queue<ll, vector<ll>, greater<ll>> pq;
    for (int i = 0; i < n; i++)
        pq.push(arr[i]);

    ll out = 0;
    while (pq.size() > 1)
    {
        ll el = pq.top();
        pq.pop();
        el += pq.top();
        pq.pop();
        out += el;
        pq.push(el);
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
