# code
def solver1(n):
    if n < 11:
        return [i for i in range(n + 1)]

    def isJumping(num):
        num_len = len(num)
        for i in range(1, num_len):
            if not (abs(ord(num[i]) - ord(num[i - 1])) == 1):
                return False
        return True

    out = [i for i in range(11)]
    i = 11
    while i < n + 1:
        if isJumping(str(i)):
            out.append(i)
        i += 1

    return out


"""
there is a pattern in series after 10,
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45 54 56 65 67 76 78 87 89 98 101 121 
123 210 212 232 234 321 323 343 345 432 434 454 456 543 545 565 567 654 656 676 
678 765 767 787 789 876

there is a pattern in it, just see the code below
"""
from queue import Queue

def solver(n):
    if n < 11:
        return [i for i in range(n + 1)]

    qu = Queue(maxsize = n + 1)
    out = [0]
    for i in range(1, 10):
        qu.put(i)
        while (not qu.empty()):
            el = qu.get()
            if el <= n:
                out.append(el)
                last = el % 10
                if last != 0:
                    qu.put(el * 10 + (last - 1))
                if last != 9:
                    qu.put(el * 10 + (last + 1))

    return sorted(out)


T = int(input())
for _ in range(T):
    n = int(input())
    print(" ".join(str(el) for el in solver(n)))
