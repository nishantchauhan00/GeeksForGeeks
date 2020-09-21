'''
For people who want the explaination for this solution, please try to solve it 
manuallly taking N=1 to 20, and you will find some pattern emerging in the 
answer index. The pattern starts emerging after 1 at every interval of 4.

SIZE INDEX(answer)
size=1, position=0
------------------------------------------------------------------------------
size=2, position=1
size=3, position=2
size=4, position=1
size=5, position=2
------------------------------------------------------------------------------
size=6, position=2
size=7, position=3
size=8, position=2
size=9, position=3
------------------------------------------------------------------------------
size=10, position=3
size=11, position=4
size=12, position=3
size=13, position=4
------------------------------------------------------------------------------
size=14, position=4
size=15, position=5
size=16, position=4
size=17, position=5
------------------------------------------------------------------------------
size=18, position=5
size=19, position=6
size=20, position=5
size=21, position=6
'''

def solver1(arr, n):
    # size are given by side
    if n == 1: # 1
        return arr[0]
    elif n%4 == 0: # 4 8 12 16 20...
        return arr[int(n/4)]
    elif n%2 == 0: # 2 6 10 14 18...
        return arr[int((n+2)/4)]
    elif (n + 1)%4 == 0: # 3 7 11 15..
        return arr[int((n + 1)/4 + 1)]
    else: # (n - 1)%4 == 0: # 5 9 13 17..
        return arr[int((n - 1)/4 + 1)]


def solver(arr, n):
    if n == 1:      # 1
        return arr[0]
    elif n%2 == 0:  # 2 4 6 8...
        return arr[(n + 2)//4]
    else:           # # n%2 == 1 # 3 5 7 9
        return arr[(n + 1)//4 + 1]



T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solver(arr, n))


