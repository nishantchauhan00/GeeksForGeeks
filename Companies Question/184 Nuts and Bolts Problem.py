'''
https://practice.geeksforgeeks.org/problems/nuts-and-bolts-problem0431/1

Comparison of a nut to another nut or a bolt to another bolt is not allowed.

'''
from functools import cmp_to_key

class Solution:
	# CHEATING, BUT FAST
	# using extra space
    # also takes care if any nut/bolt occurs more than once
	def matchPairs(self, nuts, bolts, n):
		nuts_bolts = "!#$%&*@^~"
		hmap = dict()
		for i in range(len(nuts_bolts)):
			hmap[nuts_bolts[i]] = 0
		
		for el in nuts:
			hmap[el] += 1
		
		i = 0
		for j in range(len(nuts_bolts)):
			if hmap[nuts_bolts[j]] > 0:
				for _ in range(hmap[nuts_bolts[j]]):
					nuts[i] = nuts_bolts[j]
					bolts[i] = nuts_bolts[j]
					i += 1
	

	# (use sorting with made-up comparator)
	# one thing to note is that if you dont even use comaparator the given
	# order is default order to be followed in sorting 

		



'''
1
5
@ % $ # ^
% @ # $ ^


# $ % @ ^
# $ % @ ^
'''


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1