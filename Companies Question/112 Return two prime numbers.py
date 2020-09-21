"""
https://en.wikipedia.org/wiki/Goldbach%27s_conjecture

https://practice.geeksforgeeks.org/problems/return-two-prime-numbers/0

https://www.edureka.co/blog/python-program-prime-number/

An optimization:
1) As an even number greater than 2 can't be prime, so we can skip them or have
   an incrementer of 2 instead of 1, put condition for even number greater than
   2 before
2) Instead of checking till n, we can check till √n because a larger factor of 
   n must be a multiple of smaller factor that has been already checked.
"""

def solver(n): # constraint: n is even and n >= 4
    def isPrime(num): # constraint: 2 <= num <= n/2
        if (num <= 3) :
            return True
        if (num % 2 == 0 or num % 3 == 0) :
            return False
        
        for i in range(3, int(num**(1/2)) + 1, 2): # start, end, increment
            if num % i == 0:
                return False
        return True

    # if a solution exists it will not iterate for more than n/2(exception the
    # case of n = '4'), as the pairs of (i , n-i) will start to repeat.
    for i in range(2, int(n / 2) + 1):
        if isPrime(i) and isPrime(n - i):
            return [i, n - i]

    return [-1, -1]


T = int(input())
for _ in range(T):
    n = int(input())
    print(" ".join(str(el) for el in solver(n)))
