#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int map[10] = {0};
        int n, el = 0;
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> el;
            map[el] += 1;
        }

        for (int i = 9; i >= 0; i--)
            for (int j = map[i]; j > 0; j--)
                printf("%d", i);

        printf("\n");
    }
    return 0;
}
