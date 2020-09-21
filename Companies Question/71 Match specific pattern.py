def getPattern(inpstr, n):
    j, pattern = 1, [1]
    for i in range(1, n):
        if inpstr[i] == inpstr[i - 1]:
            pattern[-1] += 1
        else:
            j += 1
            pattern.append(j)
    return pattern

# creating pattern then matching whole pattern
def findSpecificPattern1(arr, matchstr):
    out = []
    n = len(matchstr)
    matching_pattern = getPattern(matchstr, n)
    for el in arr:
        if not (len(el) == n):
            continue
        elif matching_pattern == getPattern(el, n):
            out.append(el)
    return out


# # #           OR          # # #
# match two strings with char by char, break in between if not matching
def check(matchstr, inpstr, n):
    i, j = 1, 1
    for k in range(1, n):
        if not(i == j):
            return False
        if not(matchstr[k-1] == matchstr[k]):
            i += 1
        if not(inpstr[k-1] == inpstr[k]):
            j += 1
    return True

def findSpecificPattern(arr, matchstr):
    out, n = [], len(matchstr)
    for el in arr:
        if len(el) == n and check(matchstr, el, n):
            out.append(el)
    return out


T = int(input())
for _ in range(T):
    arr = input().strip().split()
    matchstr = input().strip()
    print(" ".join(findSpecificPattern(arr, matchstr)))
