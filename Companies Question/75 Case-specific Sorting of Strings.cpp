#include <iostream>
#include <stdlib.h>
using namespace std;

string caseSort(string inpstr, int n)
{
    int lower[26] = {0}, upper[26] = {0};
    for (int i = 0; i < n; i++)
    {
        int ord = int(inpstr[i]);
        if (ord >= int('a') && ord <= int('z')) // or islower()
            lower[ord-int('a')] += 1;
        else
            upper[ord-int('A')] += 1;
    }

    string out = "";
    int x = 0, y = 0;
    for (int i = 0; i < n; i++)
    {
        while (lower[x] == 0)
            ++x;
        while (upper[y] == 0)
            ++y;

        int ord = int(inpstr[i]);
        if (ord >= int('a') && ord <= int('z'))
        {
            lower[x]--;
            out += (char)(x + int('a'));
        }
        else
        {
            upper[y]--;
            out += (char)(y + int('A'));
        }
    }

    return out;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        string inpstr;
        cin >> n;
        cin >> inpstr;
        cout << caseSort(inpstr, n) << endl;
    }
    return 0;
}

/*
2
12
defRTSersUXI
6
srbDKi
*/
