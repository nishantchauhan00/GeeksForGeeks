#include <bits/stdc++.h>
using namespace std;

int longestIncreasingSubsequence(int arr[], int n){
    
    int results[n] = {1};
    
    for(int i=1; i<n; i++)
        for(int j=0; j<i; j++)
            if (arr[i] > arr[j])
                results[i] = max(results[i], results[j] + 1);
    
    return *max_element(results, results + n);
}

int main()
{
    int t=0;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int arr[n];
        for(int i=0; i<n; i++)
            cin>>arr[i];
        cout << longestIncreasingSubsequence(arr, n) << endl;
    }
    return 0;
}
