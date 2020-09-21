# brute force approach
def getId1(m,n):
    for i in range(n):
        # find row with all elements zeroes, i.e, a celebrity who doesn't know
        # anyone
        if not(1 in m[i]):
            # make the i'th element of that row '1' for easy search
            m[i][i] = 1
            # now we confirm that everyone knows him
            for j in range(n):
                # if there is someone who doesn't know him, then return -1, 
                # because there is no possibility of other answer because
                # the current celetity knows noone
                if m[j][i] == 0:
                    return -1
            return i
    return -1

'''
using stack
https://youtu.be/LtGnA5L6LIk
'''

'''
The following observations can be made in this problem:
> If A knows B, then A can’t be celebrity. Discard A and B may be celebrity.
> If A doesn’t know B, then B can’t be celebrity. 
  Discard B, and A may be celebrity.

we will do it using O(1) space
'''
def getId(arr,n):
    candidate = 0
    for i in range(1, n):
        # if candidate knows 'i', then candidate can't be celebrity, but its 
        # possible that 'i' is celebrity 
        if arr[candidate][i] == 1:
            candidate = i
    
    # Now, we check if candidate is really a celbrity or not
    for i in range(n):
        if (i != candidate) and (arr[candidate][i] == 1 or arr[i][candidate] == 0):
            return -1   
    return candidate





# ################################
# ################################
#  Driver Code Starts
# ################################
#Initial Template for Python 3

import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        print(getId(m,n))