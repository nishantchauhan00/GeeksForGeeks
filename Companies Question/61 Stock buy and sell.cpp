#include <bits/stdc++.h>
using namespace std;

void stockBuySell(int price[], int n)
{
    int total_profit = 0;
    for (int i = 0; i < n - 1;)
    {
        // skip if price is declining or same
        while(price[i] >= price[i+1] && i<n)
            i++;
            
        int buy_at = price[i];
        int j = i, k = i + 1;
        
        while (++i < n && price[i] >= price[i-1]);

        if (price[i - 1] > buy_at)
        {
            total_profit += price[i - 1] - price[j];
            printf("(%d %d) ", j, i - 1);
        }
    }

    if (total_profit == 0)
        printf("No Profit");
    printf("\n");
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n = 0;
        cin >> n;
        int prices[n];
        for (int i = 0; i < n; i++)
            cin >> prices[i];

        stockBuySell(prices, n);

        printf("\n");
    }
    return 0;
}
