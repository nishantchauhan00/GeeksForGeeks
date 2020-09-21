# vertical scanning
def solver1(words, n):
    min_len = len(words[0])
    for w in words:
        min_len = min(min_len, len(w))

    out, i = "", 0
    # checking character by character in every word
    while i < min_len:
        for j in range(1, n):
            if words[0][i] != words[j][i]:
                return -1 if len(out) == 0 else out
        out += words[0][i]
        i += 1

    return out


# taking pairs of two word at a time, finding common, then repeating the process
# with new common and next word
def solver(words, n):
    common = words[0]

    for i in range(1, n):
        min_len = min(len(common), len(words[i]))
        j = 0
        while j < min_len:
            if common[j] != words[i][j]:
                break
            j += 1

        common = common[:j]
        if len(common) == 0:
            return -1

    return common



T = int(input())

for _ in range(T):
    n = int(input())
    words = input().split()
    print(solver(words, n))
