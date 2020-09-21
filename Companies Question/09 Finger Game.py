def finger1(n):
    out = 1
    forward = True
    while n > 1:
        if forward:
            out += 1
            if out == 5:
                forward = False
        else:
            out -= 1
            if out == 1:
                forward = True
        n -= 1
    return out


def finger(n):
    r = n % 8 # possible values: 0 to 7
    if r == 0:  # 0
        return 2
    elif r <= 5:  # 1 2 3 4 5
        return r
    else:
        if r == 6: # 6
            return 4
        elif r == 7: # 7
            return 3


"""
1  2  3  4  5
9  8  7  6  5
9 10 11 12 13

repeats after 8 as
1+8=9
2+8=10
5+8=13

so we need to hard encode till 8 then modulus works
"""


print(finger(1))
print(finger(2))
print(finger(13))
# 1 2 5
