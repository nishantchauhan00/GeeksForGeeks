#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

// brute force
vector<int> solver1(int arr[], int n)
{
    vector<int> out;
    for (int i = 1; i <= n; i++)
    {
        int j = 0, max_of_mins = -1;

        while (j + i <= n)
        {
            int curr_min = *min_element(arr + j, arr + j + i);
            max_of_mins = max(max_of_mins, curr_min);
            ++j;
        }

        out.push_back(max_of_mins);
    }

    return out;
}

// still brute force, but slightly better
// time will be half of previous brute force
// what we notice is we can discard elements from the array, by taking minumum
// of two elements and making it new array, so that we dont have to make extra
// computation again
vector<int> solver2(int arr[], int n)
{
    vector<int> out;
    out.push_back(*max_element(arr, arr + n));
    for (int i = 1; i < n; i++)
    {
        int  max_of_mins = -1;
        for (int j = n - 1; j >= i; j--){
            arr[j] = min(arr[j - 1], arr[j]);
            if (arr[j] > max_of_mins)
                max_of_mins = arr[j];
        }
        out.push_back(max_of_mins);
    }

    return out;
}


// efficient method
vector<int> solver(int arr[], int n)
{
    vector<int> out;

    int left[n], right[n];
    // left smaller
    left[0] = -1;
    int lsmall = 0;
    for(int i=1; i<n; i++){
        left[i] = lsmall;
        if (arr[lsmall] >= arr[i])
            lsmall = i;
    }

    // right smaller
    right[n-1] = n;
    int rsmall = n-1;
    for(int i=n-2; i>=0; i--){
        right[i] = rsmall;
        if (arr[rsmall] >= arr[i])
            rsmall = i;
    }

    for(int i=0; i<n; i++)
        cout<<left[i]<<"  "<<right[i]<<endl;

    return out;
}


int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        vector<int> vec;
        vec = solver(arr, n);

        for (int i = 0; i < vec.size(); i++)
            cout << vec[i] << " ";
        cout << endl;
    }
    return 0;
}
