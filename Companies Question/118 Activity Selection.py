'''
other same problem:  N meetings in one room

https://practice.geeksforgeeks.org/editorial.php?pid=296

greedy algorithm
The greedy choice is to always pick the next activity whose finish time is 
least among the remaining activities and the start time is more than or equal 
to the finish time of previously selected activity.
'''
def solver(start_finish, n):
    out, last = 0, -1
    for i in range(n):
        if start_finish[i][0] >= last:
            out += 1
            last = start_finish[i][1]
    return out


T = int(input())
for _ in range(T):
    n = int(input())
    start = list(map(int, input().split()))
    finish = list(map(int, input().split()))
    start_finish = []
    for s, f in zip(start, finish):
        start_finish.append([s, f])
    print(solver(sorted(start_finish, key=lambda el: el[1]), n))