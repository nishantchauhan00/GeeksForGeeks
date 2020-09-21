#include <iostream>
#define optimize ios_base::sync_with_stdio(0);cin.tie(NULL)
using namespace std;

// in this solution we do expansion sideways on two chosen digits 
// and whenever (sum of left == sum of right) and result is lower than current 
// length of expansion, then we update result
int solver(string str, int n)
{
    int result = 0;
    for (int i = 0; i < n - 1; i++)
    {
        int l = i, r = i + 1, lsum = 0, rsum = 0;
        while (l >= 0 && r < n)
        {
            lsum += str[l] - '0';
            rsum += str[r] - '0';
            if (lsum == rsum)
                result = max(result, r - l + 1);
            ++r;
            --l;
        }
    }
    return result;
}

int main()
{
    optimize;
    int t;
    cin >> t;
    while (t--)
    {
        string str;
        cin >> str;
        cout << solver(str, str.length()) << endl;
    }
    return 0;
}