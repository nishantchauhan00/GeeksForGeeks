T = int(input())


for _ in range(T):
    input_string = list(input())
    n = len(input_string)

    i = 0
    j = 0
    while i < n:
        while i < n and input_string[i] != '.':
            i += 1
        
        # reversing
        low = j
        high = i - 1
        while low <= high:
            input_string[low], input_string[high] = input_string[high], input_string[low] 
            low += 1
            high -= 1
        
        i += 1
        j = i
    
    print(''.join(input_string))






