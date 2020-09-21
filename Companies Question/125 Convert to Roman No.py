"""
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

constraint: n is 1 to 3999
"""
def convertRoman1(n):
    out = ""
    while n:
        if n // 1000 != 0:
            for _ in range(n // 1000):
                out += "M"
            n = n % 1000
        elif n // 500 != 0:
            if n < 900:
                out += "D"
                n = n % 500
            else:
                out += "CM"
                n = n - 900
        elif n // 100 != 0:
            if n < 400:
                for _ in range(n // 100):
                    out += "C"
                n = n % 100
            else:
                out += "CD"
                n = n - 400
        elif n // 50 != 0:
            if n < 90:
                out += "L"
                n = n % 50
            else:
                out += "XC"
                n = n - 90
        elif n // 10 != 0:
            if n < 40:
                for _ in range(n // 10):
                    out += "X"
                n = n % 10
            else:
                out += "XL"
                n = n - 40
        elif n // 5 != 0:
            if n < 9:
                out += "V"
                n = n % 5
            else:
                out += "IX"
                n = 0
        else:
            if n < 4:
                for _ in range(n):
                    out += "I"
            else:
                out += "IV"
            n = 0

    return out


'''
shorter code, same rules
'''
def convertRoman(n):
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    out = ""
    for i in range(len(nums)):
        while (n - nums[i] >= 0):
            out += romans[i]
            n-=nums[i]

    return out


T = int(input())
for _ in range(T):
    n = int(input())
    print(convertRoman(n))
