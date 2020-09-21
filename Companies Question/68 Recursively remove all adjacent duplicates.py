def solver1(inpstr, n):  #  lets first do it without recursion
    # in it we count occurences
    while True:
        if len(inpstr) == 0:
            return ""
        el = [inpstr[0]]
        occurs = [1]
        for i in range(1, len(inpstr)):
            if el[-1] == inpstr[i]:
                occurs[-1] += 1
            else:
                el.append(inpstr[i])
                occurs.append(1)

        newstr = ""
        for ch, i in zip(el, occurs):
            if i == 1:
                newstr += ch

        if newstr == inpstr:
            break
        inpstr = newstr

    return inpstr


def solver(inpstr, n):  #  lets first do it without recursion
    # in it we do not add alphabet if it occurs more than one time
    while True:
        i, j, n = 0, 0, len(inpstr)
        newstr = ""
        while i < n:
            j = i + 1
            while j < n and inpstr[i] == inpstr[j]:
                j += 1
            if j == i + 1:
                newstr += inpstr[i]
            i = j

        if newstr == inpstr:
            break
        inpstr = newstr
    return inpstr

# to apply recursion to above method just use two variable, one to track
# number of elements and other to track number of elements after removing adj
# if different call process again else return string


T = int(input())
for _ in range(T):
    inpstr = list(input())
    print(solver(inpstr, len(inpstr)))
