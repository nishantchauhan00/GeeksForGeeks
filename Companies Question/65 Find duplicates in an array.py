from collections import Counter

# from worse to better

def solver1(arr, n):
    out = []
    occurs = [0 for _ in range(n)]
    for el in arr:
        if occurs[el] == 1:
            out.append(el)
        occurs[el] += 1
    return [-1] if len(out) == 0 else sorted(out)


def solver2(arr, n):
    out = []
    counts = Counter(arr)
    for el in counts:
        if counts[el] > 1:
            out.append(el)
    return [-1] if len(out) == 0 else sorted(out)


def solver3(arr, n):
    arr = sorted(arr)
    out = [-1]
    for i in range(1, n):
        if arr[i] == arr[i-1] and not(out[-1] == arr[i]):
            out.append(arr[i])
    return out if len(out) == 1 else out[1:]


# we can take advantage of the constraint that arr[i] lies between 0 to n 
def solver(arr, n):
    # we will increase the element by n at the index equal to the value of element, 
    # if it occurs more than one time then arr[i]/n will be greater than 1, because
    # 'n' is added 2 or more times
    for i in range(n):
        index = arr[i] % n
        arr[index] += n 
    
    out = []
    for i in range(n):
        # the index is the element
        if arr[i]//n > 1:
            out.append(i)

    return [-1] if len(out) == 0 else out


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(" ".join(str(el) for el in solver(arr, n)))
