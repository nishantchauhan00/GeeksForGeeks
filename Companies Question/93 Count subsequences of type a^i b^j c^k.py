# https://www.geeksforgeeks.org/number-subsequences-form-ai-bj-ck/

'''
In this question, we will maintain 3 variables and then ouput 3rd variable.
aa, ab, bc = 0, 0, 0

>aa is number of possible ways if new single 'a' is followed by previous aa ways
aa = 2*aa + 1
(new ways possible if 'a' append to previous ways + 1 way if previous not counted)

>ab is if 'b' is followed by previous 'aa...aabb..b' ways
ab = 2*ab + aa
(new ways if 'b' followed by previous ways + aa ways if only new single b follows
aa ways)

>similarly for bc c followed by 'aaa..abbb..bccc..c' ways
bc = 2*bc + ab
(new ways if 'c' followed by previous ways + ab ways if only new single 'c'
 follows ab ways)

so at last bc consists of ways to form 'aa..abb..bcc..c' ways
'''
def solver(inpstr):
    aa, ab, bc = 0, 0, 0
    for i in range(len(inpstr)):
        if inpstr[i] == 'a':
            aa = 2*aa + 1
        elif inpstr[i] == 'b':
            ab = 2*ab + aa
        else: # inpstr[i] == 'b':
            bc = 2*bc + ab
    
    return bc


T = int(input())

for _ in range(T):
    inpstr = input()
    print(solver(inpstr))
