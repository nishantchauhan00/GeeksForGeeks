#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

#define ll long long

string idToURL(ll n)
{
    string url = "";
    while (n > 0)
    {
        ll rem = n % 62;
        n = (n - rem) / 62;
        // cout<<rem<<endl;
        if (rem >= 0 && rem <= 25)
            url += (char)(rem + int('a'));
        else if (rem >= 26 && rem <= 51)
            url += (char)(rem + int('A') - 26);
        else
            url += (char)(rem + int('0') - 52);
    }
    reverse(url.begin(), url.end());
    return url;
}

ll urlToID(string url)
{
    ll id = 0, slen = url.length();
    for (ll i = 0; i < slen; i++)
    {
        ll order = 0;
        if (url[i] >= int('a') && url[i] <= int('z'))
            order = int(url[i]) - int('a');
        else if (url[i] >= int('A') && url[i] <= int('Z'))
            order = int(url[i]) - int('A') + 26;
        else
            order = int(url[i]) - int('0') + 52;

        id += (ll)(0.5 + pow(62, slen - i - 1)) * order;
    }
    return id;
}

int main()
{
    int t;
    scanf("%d\n", &t);
    while (t--)
    {
        int n;
        cin >> n;

        string url = idToURL(n);
        int id = urlToID(url);
        cout << url << endl
             << id << endl;
    }
    return 0;
}