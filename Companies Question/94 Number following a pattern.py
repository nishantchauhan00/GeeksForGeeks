'''
We can that when we encounter I, we got numbers in increasing order but if we 
encounter ‘D’, we want to have numbers in decreasing order. Length of the output 
string is always one more than the input string. So loop is from 0 till the 
length of the sting. We have to take numbers from 1-9 so we always push (i+1) 
to our stack. Then we check what is the resulting character at the specified 
index.So,there will be two cases which are as follows:-

Case 1: If we have encountered I or we are at the last character of input string,
then pop from the stack and add it to the end of the output string until the 
stack gets empty.

Case 2: If we have encountered D, then we want the numbers in decreasing order.
so we just push (i+1) to our stack.
'''
def solver(inpstr, n):
    stack = []
    out = ""
    for i in range(n+1):
        stack.append(i+1)
        print(stack)
        if i == n or inpstr[i] == 'I':
            while len(stack) > 0:
                out += str(stack[-1])
                stack.pop() 
    return out


T = int(input())

for _ in range(T):
    inpstr = input()
    print(solver(inpstr, len(inpstr)))
