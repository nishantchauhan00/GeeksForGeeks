#code
'''
int dp[n];

if( n == 1 )
    cout << a[0] << endl;
elif( n == 2 )
    cout << max(a[0],a[1]) << endl;
else{
    dp[0] = a[0];
    dp[1] = max(a[0],a[1]);

    for( int i = 2; i < n; i++ )
        dp[i] = max(dp[i-1], (a[i]+dp[i-2]));

    cout << dp[n-1] << endl;
}
'''

def solver(arr, n):
    incl = 0
    excl = 0
    
    for i in arr:
        new_incl = max(incl,excl)
        incl = excl + i
        excl = new_incl
        
    return max(incl,excl)


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solver(arr, n))




