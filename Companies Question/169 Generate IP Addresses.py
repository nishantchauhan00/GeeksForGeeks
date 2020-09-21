"""
THE VALIDITY OF IPV4-->

1-->THERE MUST BE EXACTLY 3 DECIMAL POINTS ;
2-->EACH NUMBER BETWEEN TWO CONSECUTIVE DECIMAL POINT MUST BE LESS THAN OR 
    EQUAL TO 255 ;
3-->NO NUMBER SHOULD START FROM 0 EXCEPT .0. ;
"""
# Your Function should return a list containing all possible IP address
# No need to worry about order
def genIP(s):
    ip_list = []
    if len(s) < 4:
        return ip_list

    def helper(i, decimals, ip, n):
        # print(i, decimals, ip, n)
        if decimals == 3:
            if i != n: 
                if s[i] == '0':
                    if i == n-1:
                        ip_list.append(ip + s[i:])
                else:
                    if int(s[i:]) <= 255:
                        ip_list.append(ip + s[i:])
            return

        if s[i] == '0':
            helper(i + 1, decimals + 1, ip + s[i] + ".", n)
        else:
            for j in range(i, n + decimals - 2):
                if int(s[i:j+1]) > 255:
                    return
                helper(j + 1, decimals + 1, ip + s[i : j + 1] + ".", n)

    helper(0, 0, "", len(s))
    # print(ip_list)
    return ip_list





if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = genIP(s)
        res.sort()
        for u in res:
            print(u)
