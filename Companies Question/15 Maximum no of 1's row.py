T = int(input())


for _ in range(T):
    row, col = list(map(int, input().split()))
    arr = input().split()

    maxrow = 0
    maxone = 0
    for i in range(row):
        start = col*i
        while arr[start] == '0':
            start += 1
        
        ones = col*(i+1) - start

        if ones > maxone:
            maxone = ones
            maxrow = i

    print(maxrow)



