#include <iostream>
using namespace std;

// only case when not possible is when maximum present character is more
// than half of length
int solver(string inp)
{
    int counts[26] = {0}, n = inp.size();
    for (int i = 0; i < n; i++)
        counts[inp[i] - 'a']++;

    int maxc = 0;
    for (int i = 0; i < 26; i++)
        if (maxc < counts[i])
            maxc = counts[i];

    if (n % 2 != 0)
        ++n;

    return (maxc > n / 2) ? 0 : 1;
}

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        string inp;
        cin >> inp;

        cout << solver(inp) << endl;
    }
    return 0;
}