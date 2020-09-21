def solver(n):
    out = ""
    while n > 0:
        x = n % 26
        if x is not 0:
            out += chr(x + 64)
            n = int(n/26)
        else: # if x is 0:
            out += 'Z'
            n = int(n/26) - 1
    return out[::-1]


T = int(input())

for _ in range(T):
    N = int(input())
    print(solver(N))


'''
https://www.geeksforgeeks.org/find-excel-column-name-given-number/

> Suppose we have a number n, let’s say 28. so corresponding to it we need to print 
the column name. We need to take remainder with 26.
> If remainder with 26 comes out to be 0 (meaning 26, 52 and so on) then we put ‘Z’ 
in the output string and new n becomes n/26 -1 because here we are considering 26 
to be ‘Z’ while in actual it’s 25th with respect to ‘A’.

Similarly if the remainder comes out to be non zero. (like 1, 2, 3 and so on) then 
we need to just insert the char accordingly in the string and do n = n/26.
Finally we reverse the string and print.
'''

