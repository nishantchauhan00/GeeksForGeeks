'''
Note: Order does not matter means for n=4 {1 2 1},{2 1 1},{1 1 2} 
are considered same.
https://practice.geeksforgeeks.org/problems/count-ways-to-nth-stairorder-does-not-matter/0/
'''

# bruteforce, recursion
# the WORST WAY
def solver1(n):
    ways = set()
    def helper(i = 0, way = []):
        if i == n:
            ways.add(tuple(sorted(way)))
            return
        if i > n:
            return

        helper(i + 1, way + [1])
        helper(i + 2, way + [2])

    helper()
    return len(ways)


'''
number - steps
0 - 1
1 - 1
2 - 2
3 - 2
4 - 3
5 - 3
6 - 4
7 - 4
8 - 5
9 - 5
10 - 6
11 - 7
12 - 7

we saw a pattern here

'''
def solver(n):
    # return int((n+2)/2)
    # OR
    return n//2 + 1


'''
it can be done using dp too

Solution:
> Consider a position i. No. of ways to reach i will be sum of ways to reach  
  i - 2 and 1 (as order does not matter)
> So store the values in a DP array and compute till the required value.

but what i did above is king of same solution but shorter way
'''





for _ in range(int(input())):
    n = int(input())
    print(solver(n))
