def solver(n):
    if n < 3: # 
        return n

    out = 1
    while n > 1:
        if n % 2 is not 0:
            return -1
        n = n / 2
        out += 1
    return out


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(solver(n))


