def solver(inpstr):
    out = []

    def helper(l=0, r=len(inpstr) - 1):
        if l == r:
            out.append("".join(inpstr))
        else:
            for i in range(l, r+1):
                inpstr[l], inpstr[i] = inpstr[i], inpstr[l]
                helper(l + 1, r)
                inpstr[l], inpstr[i] = inpstr[i], inpstr[l]

    helper()
    return out


if __name__ == "__main__":
    inp = list(input())
    print(" ".join(solver(inp)))
