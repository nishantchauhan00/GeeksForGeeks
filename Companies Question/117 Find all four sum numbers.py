# code, brute force
# test cases aren't good as it is also passing, 0.34s
def solver1(arr, n, k):
    out = set()
    if n < 4:
        return out
    arr.sort()
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if arr[a] + arr[b] + arr[c] + arr[d] == k:
                        out.add((arr[a], arr[b], arr[c], arr[d]))
    return sorted(out)


# recursive solution for sum of any amount of numbers
# gives tle
def solver2(arr, n, k, n_len=4):
    out = set()
    arr.sort()

    def helper(i, els, sum_now, els_n):
        if els_n == n_len:
            if sum_now == k:
                out.add(tuple(els))
            return
        if i == n:
            return
        helper(i + 1, els + [arr[i]], sum_now + arr[i], els_n + 1)
        helper(i + 1, els, sum_now, els_n)

    helper(0, [], 0, 0)
    return sorted(out)


# two pointer solution, 0.05s
def solver3(arr, n, k, n_len=4):
    out = set()
    if n < 4:
        return out
    arr.sort()
    for i in range(n-3):
        for j in range(i + 1, n-2):
            l, r = j + 1, n - 1
            s1 = arr[i] + arr[j]
            while l < r:
                s = s1 + arr[l] + arr[r]
                if s == k:
                    out.add((arr[i], arr[j], arr[l], arr[r]))
                    l += 1
                    r -= 1
                elif s < k:
                    l += 1
                else:  # s > k
                    r -= 1

    return sorted(out)


# hashmap based approach, 0.03s
# finding two sum instead of four sum
def solver(arr, n, k, n_len=4):
    out = set()
    if n < 4:
        return out
    hmap = {}
    for i in range(n-1):
        for j in range(i + 1, n):
            s=arr[i] + arr[j]
            if s in hmap:
                hmap[s].append([i, j])
            else:
                hmap[s] = [[i, j]]
    
    for i in range(n-3):
        for j in range(i + 1, n-2):
            diff = k - (arr[i] + arr[j])
            if diff in hmap:
                for index in hmap[diff]:
                    if (index[0] != i) and (index[0] != j) and (index[1] != i) and (index[1] != j):
                        res = sorted((arr[i], arr[j], arr[index[0]], arr[index[1]]))
                        out.add(tuple(res))
    return sorted(out)


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    out = solver(arr, n, k)
    if len(out) == 0:
        print("-1")
    else:
        print(" $".join(" ".join(str(el) for el in tup) for tup in out), end=" $\n")
