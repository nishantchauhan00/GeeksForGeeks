"""
Given three strings A, B and C your task is to complete the function 
isInterleave which returns true if C is an interleaving of A and B else returns 
false. C is said to be interleaving A and B, if it contains all characters of 
A and B and order of all characters in individual strings is preserved.
"""


def solver(A, B, C):
    n1, n2, n3 = len(A), len(B), len(C)

    def helper(i, j, k, out = 0):
        if k == n3:
            return 1
        else:
            if i < n1 and A[i] == C[k]:
                out = max(out, helper(i + 1, j, k + 1, out))
            if j < n2 and B[j] == C[k]:
                out = max(out, helper(i, j + 1, k + 1, out))
            return out

    return helper(0, 0, 0) 
    


T = int(input())

for _ in range(T):
    A, B, C = input().split()
    print(solver(A, B, C))
