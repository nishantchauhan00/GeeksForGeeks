def solver(words, n, inp):
    i, j, n1 = 0, 1, len(inp)
    # inp_words = []
    while j <= n1:
        if inp[i:j] in words:
            # inp_words.append(inp[i:j])
            i = j
        j += 1

    # print(inp_words) # contains list of separated words given in input
    return 1 if i == n1 else 0 



T = int(input())
for _ in range(T):
    n = int(input())
    words = input().split()
    inp = input()
    print(solver(words, n, inp))

