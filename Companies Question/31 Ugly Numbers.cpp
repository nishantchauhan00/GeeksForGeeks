#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long int nthUglyNumber(int n)
    {
        if (n < 7)
            return n;
        
        int t2 = 0, t3 = 0, t5 = 0;
        long int K[n];
        K[0] = 1;
        for (int i = 1; i < n; i++)
        {
            K[i] = min(K[t2] * 2, min(K[t3] * 3, K[t5] * 5));
            if (K[i] == K[t2] * 2)
                t2++;
            if (K[i] == K[t3] * 3)
                t3++;
            if (K[i] == K[t5] * 5)
                t5++;
        }
        return K[n - 1];
    }
};

int main() {
	Solution s;
	int t;
	scanf("%d", &t);
	while (t--){
	    int n;
	    scanf("%d", &n);
	    cout<<s.nthUglyNumber(n)<<endl;
	}
	return 0;
}