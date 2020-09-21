# indian multiplication method in efficient way

def multiply(num1, num2):
    # checking sign
    sign = 1
    if num1[0] == "-":
        num1 = num1[1:]
        sign *= -1
    if num2[0] == "-":
        num2 = num2[1:]
        sign *= -1
    
    # if any number contains only zero
    i = 0
    while i < len(num1) and num1[i] =='0':
        if i == len(num1) - 1:
            return "0"
        i += 1
    i = 0
    while i < len(num2) and num2[i] =='0':
        if i == len(num2) - 1:
            return "0"
        i += 1
    
    #placeholder for multiplication ndigit by mdigit result in n + m digits
    product = [0] * (len(num1) + len(num2)) 
    
    # position within the placeholder
    position = len(product)-1 

    for n1 in num1[::-1]:
        tempPos = position 
        for n2 in num2[::-1]: 
            # ading the results of single multiplication
            product[tempPos] += int(n1) * int(n2) 
            
            # bring out carry number to the left array
            product[tempPos-1] += product[tempPos]//10 
            
            product[tempPos] %= 10 # remove the carry out from the current array
            
            # first shifting the multplication to the end of the first integer
            tempPos -= 1 

        # then once first integer is exhausted shifting the second integer and 
        # starting 
        position -= 1 


    # once the second integer is exhausted we want to make sure we are not zero padding  
    pointer = 0 # pointer moves through the digit array and locate where the zero padding finishes
    while pointer < len(product)-1 and product[pointer] == 0: 
        # if we have zero before the numbers shift the pointer to the right
        pointer += 1

    return  ("-" if sign == -1 else "") + ''.join(map(str, product[pointer:])) # only report the digits to the right side of the pointer



# 
# 
# i tried to implement indian multiplication method
# 
class Solution:
    def multiply(self, a, b):
        sign = 1
        if a[0] == "-":
            a = a[1:]
            sign *= -1
        if b[0] == "-":
            b = b[1:]
            sign *= -1

        if a[0] == "0" or b[0] == "0":
            return "0"

        out = ""

        left = "0"
        for i in range(len(b) - 1, -1, -1):
            temp = self.mult(a, b[i])
            # --TO BE IMPLEMENTED --
            # add_num
            temp = str(int(temp) + int("0" + left))
            out += temp[-1]
            left = temp[:-1]

        out += left[::-1]

        if sign == -1:
            out += "-"
        return out[::-1]

    # # --TO BE IMPLEMENTED --
    # # add_num
    # def add_nums(self, a, b):
    #     if len(a) < len(b):

    def mult(self, n, x):
        carry = "0"
        out = ""
        x = ord(x) - 48
        for i in range(len(n) - 1, -1, -1):
            temp = str((ord(n[i]) - 48) * x + self.intof(carry))
            carry = temp[:-1]
            out += temp[-1]
        if self.intof(carry) != 0:
            out += carry
        return out[::-1]

    def intof(self, n):
        num = 0
        mul = 1
        for i in range(len(n) - 1, -1, -1):
            num += (ord(n[i]) - 48) * mul
            mul *= 10
        return num


s = Solution()
print(s.multiply("9", "5"))
