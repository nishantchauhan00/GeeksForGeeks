#include <iostream>
#include <unordered_map>
#include <math.h>
#define ll long long
using namespace std;

/*
There is a pattern in binary representation of the number that can be used to 
find if number is a multiple of 3. If difference between count of odd set bits 
(Bits set at odd positions) and even set bits is multiple of 3 then is the 
number.
*/
class Solution
{
public:
    // the bad solution, it won't work if size of s is large
    int isDivisible1(string s)
    {
        ll num = 0;
        ll n = s.size();
        for (char el : s)
        {
            if (el == '1')
                num += pow(2, n);
            n -= 1;
        }

        return (num % 3 == 0) ? 1 : 0;
    }

    int isDivisible(string s)
    {
        ll i = 0, n = s.size();

        // to pass extra zeroes in front of binary number string
        while (i < n && s[i] == '0')
            i++;

        // first bit will be on 1st place and '1' is odd number so odd is true
        // at first, if odd is false then it is even position
        bool odd = true;
        ll even_set = 0, odd_set = 0;
        while (i < n)
        {
            if (odd) { // odd
                if (s[i] == '1')
                    ++even_set;
                odd = false;
            }
            else { // even
                if (s[i] == '1')
                    ++odd_set;
                odd = true;
            }
            ++i;
        }

        ll diff = even_set - odd_set;
        return (diff % 3 == 0) ? 1 : 0;
    }
};

int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        Solution ob;
        cout << ob.isDivisible(s) << endl;
    }
    return 0;
}