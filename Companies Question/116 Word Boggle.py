# recursion, 0.06s
# its a kind of DFS as we are traversing the position which isn't traversed before
# i have used sets for dictionary, although trie is preferrable for dictionary,
# you only have to traverse further if character or string is part of trie
def solver(arr, row, col, words, n_max): 
    out = set()
    vis = [[-1 for _ in range(col)] for _ in range(row)]
    def helper(i, j, word):
        if word in words:
            out.add(word)
        if i < 0 or i >= row or j < 0 or j >= col or (len(word) > n_max) or (vis[i][j] == 1):
            return
        vis[i][j] = 1
        helper(i-1, j-1, word + arr[i][j])
        helper(i-1, j, word + arr[i][j])
        helper(i-1, j+1, word + arr[i][j])
        helper(i, j+1, word + arr[i][j])
        helper(i+1, j+1, word + arr[i][j])
        helper(i+1, j, word + arr[i][j])
        helper(i+1, j-1, word + arr[i][j])
        helper(i, j-1, word + arr[i][j])
        vis[i][j] = -1
        
    for i in range(row):
        for j in range(col):
            helper(i, j, "")
    return sorted(out)


T = int(input())

for _ in range(T):
    n = int(input())
    words = set(input().split())
    n_max = 0
    for word in words:
        n_max = max(n_max, len(word))
        
    row, col = map(int, input().split())
    temparr = input().split()
    
    arr = [[None for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            arr[i][j] = temparr[i * col + j]
    
    out = solver(arr, row, col, words, n_max)
    if len(out) > 0:
        print(" ".join(el for el in out))
    else:
        print("-1")
        
        