def solver(h, m):
    hour_1 = 30
    minute_1 = 6
    
    hour_angle = hour_1 * (h + ((m % 60) / 60))
    minute_angle = minute_1 * m

    diff = abs(hour_angle - minute_angle)
    
    return int(min(diff, 360-diff))


T = int(input())
for _ in range(T):
    h, m = map(float, input().split())
    print(solver(h, m))


'''
3
9 60
3 30
12 21.1274


90
75
116
'''