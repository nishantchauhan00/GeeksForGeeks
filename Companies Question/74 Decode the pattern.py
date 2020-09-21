def solver(n):
    def nextSequence(sequence):
        out = ""
        i, n = 0, len(sequence)
        while i < n:
            char, j = sequence[i], 0
            while i < n and sequence[i] == char:
                j += 1
                i += 1
            out += str(j) + char
        return out

    sequence = "1"
    for _ in range(n - 1):
        sequence = nextSequence(sequence)
    return sequence



if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(solver(n))
