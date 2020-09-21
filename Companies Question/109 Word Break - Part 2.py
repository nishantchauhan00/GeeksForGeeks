# using recursion
def solver(words, n, inp, n1):
    def helper(i, curr, ans):
        curr += inp[i]
        if i == n1 - 1: # end of input string
            if curr in words:
                print("(" + ans + curr + ")", end="")
            return
        else:
            if curr in words: # make curr empty when found and attach to answer
                helper(i + 1, "", ans + curr + " ")
            helper(i + 1, curr, ans)

    helper(0, "", "")


# it do not check for no solution in which we have to print "EMPTY"
T = int(input())
for _ in range(T):
    n = int(input())
    words = input().split()
    inp = input()
    solver(words, n, inp, len(inp))
    print()
