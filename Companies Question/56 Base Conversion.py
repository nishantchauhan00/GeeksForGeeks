"""
Each test case contains  4 space separated integers, A in decimal, B binary,C 
decimal and D hexadecimal respectively.

Output: Print 4 space separated integers representing the binary equivalent of 
A, decimal equivalent of B, hexadecimal equivalent of C and decimal equivalent 
of D respectively.
"""
def solver(A, B, C, D):
    def decimal2binary(n):
        binary = ""
        while n > 0:
            binary += str(n % 2)
            n = n // 2
        return binary[::-1]

    def binary2decimal(n):
        n = list(str(n))
        decimal, j = 0, 0
        for i in range(len(n) - 1, -1, -1):
            decimal += int(n[i]) * (2 ** j)
            j += 1
        return str(decimal)

    def decimal2hexadecimal(n):
        hexadecimal = ""
        after10 = ["A", "B", "C", "D", "E", "F"]
        while n > 0:
            temp = n % 16
            if temp < 10:
                hexadecimal += str(temp)
            else:
                hexadecimal += after10[temp - 10]
            n = n // 16
        return hexadecimal[::-1]

    def hexadecimal2decimal(n):
        decimal, j = 0, 0
        for i in range(len(n) - 1, -1, -1):
            el_ord = ord(n[i])
            if el_ord >= 48 and el_ord <= 57:
                decimal += int(n[i]) * (16 ** j)
            else:
                decimal += (el_ord - 65 + 10) * (16 ** j)
            j += 1
        return str(decimal)

    return [
        decimal2binary(A),
        binary2decimal(B),
        decimal2hexadecimal(C),
        hexadecimal2decimal(D),
    ]


T = int(input())
for _ in range(T):
    A, B, C, D = input().split()
    print(" ".join(str(el) for el in solver(int(A), int(B), int(C), list(D))))
