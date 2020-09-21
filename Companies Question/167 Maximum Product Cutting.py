'''
https://practice.geeksforgeeks.org/editorial.php?pid=2321
'''

# recursion
def solver1(n):
    if (n == 0 or n == 1):
        return 0

    max_prod = 0
    for i in range(1, n):
        # (either cut into two parts) or (take firstpart * max of secondpart)
        max_prod = max(max_prod, max(i * (n - i), i * solver1(n - i)))

    return max_prod




for _ in range(int(input())):
    n = int(input())
    print(solver1(n))
