#include <iostream>
#include <vector>
using namespace std;

/*
https://www.geeksforgeeks.org/find-two-non-repeating-elements-in-an-array-of-repeating-elements/

All the bits that are set in xor will be set in one non-repeating element 
(x or y) and not in others. So if we take any set bit of xor and divide the 
elements of the array in two sets – one set of elements with same bit set and 
another set with same bit not set. By doing so, we will get x in one set and y 
in another set. Now if we do XOR of all the elements in the first set, we will 
get the first non-repeating element, and by doing same in other sets we will 
get the second non-repeating element.

Ex: 2  4  7  4  9  2
xor of above will be 14 = '1110' = 7^9, (7 = 0111,  9 = 1001)
as xor of same digits is zero, xor of something with zero change nothing and 
only non repeating digit will be left, i.e., 7 and 9.

So, take any bit which is 1(this bit will occur in one number and not in another).

Lets take rightmost on bit.(2nd LSB in above example is on in 7, not in 9).
To find set bit number: set_bit_no = xor & ~(xor-1) = (1110) & ~(1101) = 0010

Now take two lists, put all number with bit = 1 at that position, and bit = 0
at that position.
XOR of first list should give first number and XOR of second list give second
number.
*/
void solver1(int arr[], int n)
{
    int xor_a_b = arr[0];
    for (int i = 1; i < n; i++)
        xor_a_b ^= arr[i];

    // right most on position
    int pos = xor_a_b & (~(xor_a_b - 1));
    vector<int> ON_at_pos, OFF_at_pos;

    for (int i = 0; i < n; i++)
    {
        if (pos & arr[i])
            ON_at_pos.push_back(arr[i]);
        else
            OFF_at_pos.push_back(arr[i]);
    }

    int a = 0, b = 0;
    for (int i = 0; i < ON_at_pos.size(); i++)
        a ^= ON_at_pos[i];
    for (int i = 0; i < OFF_at_pos.size(); i++)
        b ^= OFF_at_pos[i];

    printf("%d %d\n", min(a, b), max(a, b));
}

/*
little optimizations:
> as we have xor of all numbers of array, then doing one more xor of it
with a will give b, so we need only one vector
> instead of maintaining vector, just directly do xor with a or b.
*/
void solver(int arr[], int n)
{
    int xor_a_b = arr[0];
    for (int i = 1; i < n; i++)
        xor_a_b ^= arr[i];

    // right most on position
    int pos = xor_a_b & (~(xor_a_b - 1));

    int a = 0, b = 0;
    for (int i = 0; i < n; i++)
    {
        if (pos & arr[i])
            a ^= arr[i];
        else
            b ^= arr[i];
    }

    printf("%d %d\n", min(a, b), max(a, b));
}

int main()
{
    int t;
    scanf("%d\n", &t);
    while (t--)
    {
        int k, n;
        scanf("%d\n", &k);
        n = 2 * k + 2;
        int arr[n];
        for (int i = 0; i < n; i++)
            scanf("%d ", &arr[i]);

        solver(arr, n);
    }
    return 0;
}