def inc(left):
    leftlist = list(left)
    last = len(left) - 1
    while leftlist[last] == '9':
        leftlist[last] = '0'
        last -= 1

    leftlist[last] = str(int(leftlist[last]) + 1)
    return "".join(leftlist)


def solver(number, n):
    size = len(number)
    odd = size % 2
    if odd:
        center = number[int(size / 2)]
    else:
        center = ''
    left = number[:int(size / 2)]
    right = left[::-1]
    pdrome = left + center + right
    
    if pdrome > number:
        print(" ".join(list(pdrome)))
    else:
        if center:
            if center < '9':
                center = str(int(center) + 1)
                print(" ".join(list(left + center + right)))
                return
            else:
                center = '0'
        if left == len(left) * '9':
            print(" ".join(list('1' + (len(number) - 1) * '0' + '1')))
        else:
            left = inc(left)
            print(" ".join(list(left + center + left[::-1])))



for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    solver("".join(str(el) for el in arr), n)


'''
7
11
9 4 1 8 7 9 7 8 3 2 2
3
1 1 0
3
1 2 1
4
9 9 9 9
2
2 3
4
2 3 4 8
4
2 3 2 1

Output:
9 4 1 8 8 0 8 8 1 4 9
1 1 1
1 3 1
1 0 0 0 1
3 3
2 4 4 2
2 3 3 2
'''