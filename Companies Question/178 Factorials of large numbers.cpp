#include <iostream>
using namespace std;

class Solution
{
public:
    // simple straight method
    // DOESN'T WORK
    int factorial1(int n)
    {
        if (n <= 2)
            return n;

        int out = 1;
        while (n)
            out *= n--;
        return out;
    }

    ///////////////////////////////////
    // USING STRING MANIPULATION ///////////////////////////////////
    ///////////////////////////////////
    string mult(string n1, int n)
    {
        string n_str = to_string(n);
        int total_len = n1.size() + n_str.size();
        int last_index = total_len - 1;

        char out[total_len+1];
        for(int i=0; i < total_len; i++)
            out[i] = '0'; 
        out[total_len] = '\0';

        for (int i = n_str.size() - 1; i >= 0; --i)
        {
            int index = last_index;
            int val = (n_str[i] - '0');

            int carry = 0;
            for (int j = n1.size() - 1; j >= 0; --j, --index)
            {
                int curr = val*(n1[j] - '0') + carry + (out[index] - '0');
                carry = curr/10;
                out[index] = (char)(curr%10 + '0');
                // cout<<total_len<<" "<<index<<" "<<curr%10<<" "<<val<<" "<<(n1[j] - '0')<<" "<<curr<<" "<<carry<<endl;
            }

            if (carry > 0)
                out[index] = (char)(carry + '0');

            // cout<<i<<" "<<out<<endl;
            --last_index;
        }

        return out;
    }

    string factorial(int n)
    {
        string out = "1";
        while (n)
        {
            out = mult(out, n);
            --n;
        }
        
        int i = 0;
        while(out[i] == '0')
            i++;
        return out.substr(i);
    }
};

int main()
{
    int t;
    cin >> t;
    Solution obj;
    while (t--)
    {
        int N;
        cin >> N;
        cout << obj.factorial(N) << endl;
    }
    return 0;
}