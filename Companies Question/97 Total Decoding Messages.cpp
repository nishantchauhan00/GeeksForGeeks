#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
/*
Recur from end

1) If the last digit is non-zero, recur for remaining (n-1) digits and add the 
result to total count.
2) If the last two digits form a valid character (or smaller than 27), recur 
for remaining (n-2) digits and add the result to total count.
*/
int solver1(string inp, int n, int i)
{
    if (i <= 1)
        return 1;

    int out = 0;
    if (inp[i - 1] != '0') // if non zero, consider the current digit alone
        out = solver1(inp, n, i - 1);

    // if its makes sense with previous digit, consider them both together
    if (inp[i - 2] == '1' || (inp[i - 2] == '2' && inp[i - 1] < '7'))
        out += solver1(inp, n, i - 2);

    return out;
}

// If we take a closer look at the above program, we can observe that the
// recursive solution is similar to Fibonacci Numbers.
int solver(string inp, int n)
{
    int dp[n + 1] = {0};
    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i < n + 1; i++)
    {
        if (inp[i - 1] != '0') // if non zero, consider the current digit alone
            dp[i] += dp[i - 1];

        // if its makes sense with previous digit, consider them both together
        if (inp[i - 2] == '1' || (inp[i - 2] == '2' && inp[i - 1] < '7'))
            dp[i] += dp[i - 2];
    }

    return dp[n];
}

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        int n;
        string inp;
        cin >> n >> inp;

        if (inp[0] == '0')
            cout <<"0" << endl;
        else
            // cout << solver1(inp, n, n) << endl;
            cout << solver(inp, n) << endl;
    }
    return 0;
}