/* 
# tle on geeks, so using cpp now


def solver(cents, V, N):
    counts = set()
    def helper(until = 0, count = 0):
        if until == V:
            counts.add(count)
        else:
            for el in cents:
                if el + until <= V:
                    helper(until + el, count + 1)

    helper()

    return min(counts)


T = int(input())

for _ in range(T):
    V, N = list(map(int, input().split()))
    cents = list(map(int, input().split()))
    print(solver(cents, V, N))
*/



#include <bits/stdc++.h>
using namespace std;

void fast()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

// recursion
static int out = INT_MAX;
void solver(int coin[], int V, int N, int until = 0, int count = 0)
{
    if (until == V)
        out = min(out, count);
    else
        for (int i = 0; i < N; i++)
            if (coin[i] + until <= V)
                solver(coin, V, N, until + coin[i], count + 1);
}

// dp
int minCoins(int coins[], int m, int V)
{
    // table[i] will be storing the minimum number of coins
    // required for i value.  So table[V] will have result
    int table[V + 1];

    // Base case (If given value V is 0)
    table[0] = 0;

    // Initialize all table values as Infinite
    for (int i = 1; i <= V; i++)
        table[i] = INT_MAX;

    // Compute minimum coins required for all
    // values from 1 to V
    for (int i = 1; i <= V; i++)
    {
        // Go through all coins smaller than i
        for (int j = 0; j < m; j++)
            if (coins[j] <= i)
            {
                // subres is minmum no. of change for (i-coin_el) values/coins
                int sub_res = table[i - coins[j]];
                // we will update the current value if its lower than subres+1
                if (sub_res != INT_MAX)
                    table[i] = min(table[i], sub_res + 1);
            }
    }
    return (table[V] == 2147483647) ? -1 : table[V];
}

int main()
{
    fast();
    int t;
    scanf("%d\n", &t);
    while (t--)
    {
        int v, n;
        scanf("%d %d\n", &v, &n);
        int coin[n];
        for (int i = 0; i < n; i++)
            scanf("%d ", &coin[i]);
        printf("%d\n", minCoins(coin, n, v));
        // solver(coin, v, n);
        // printf("%d\n", out);
        // out = v;
    }
    return 0;
}