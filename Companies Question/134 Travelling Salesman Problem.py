INT_MAX = 99999999
'''
we have to form hamiltonian cycle in this problem

In other words, the problem is: Given a  complete graph with weighted edges 
(as an  adjacency matrix) what is the Hamiltonian  cycle (path that visits 
every node once) of  minimum cost.
'''
# O(n!)
def solver(arr, n): 
    vis = [False for _ in range(n)]
    vis[0] = True

    min_cost = INT_MAX
    def helper(i, cost, vis_count):
        nonlocal min_cost
        if cost > min_cost: # prune too many non-desirable costly paths
            return INT_MAX
        if vis_count == n:
            cost += arr[i][0]
            return cost

        for j in range(n):
            if not vis[j]:
                vis[j] = True
                min_cost = min(min_cost, helper(j, cost + arr[i][j], vis_count + 1))
                vis[j] = False

        return min_cost

    return helper(0, 0, 1)



'''
lets try greedy on it using nearest neighbour
although gives pretty good result but not optimal
DOESN'T WORK

def solver(arr, n):
    for i in range(n):
        arr[i][i] = INT_MAX

    cost = INT_MAX
    for start in range(n):
        vis_count, curr_cost = 1, 0
        last = start
        vis = [False for _ in range(n)]
        vis[start] = True # mark start node visited
        while vis_count < n:
            i = 0
            while vis[i]:
                i += 1
            for j in range(i, n):
                if not vis[j] and arr[last][j] < arr[last][i]:
                    i = j
            vis[i] = True
            curr_cost += arr[last][i]
            last = i
            vis_count += 1
        curr_cost += arr[last][start] # again go back to start
        cost = min(cost, curr_cost)
    
    return cost
'''



for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    mat = []
    for i in range(0, n * n, n):
        mat.append(lis[i : i + n])
    print(solver(mat, n))
