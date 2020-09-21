# I think some problem is there in this code
# 
# 

def findSCC(graph, V):
    # to track if a value is on stack or not
    onStack = [False for _ in range(V)]
    stack = []  # stack

    UNVISITED = None
    # ids store new ids we will assign, not old ids
    # ids will also help to know if a node has been visited or not
    ids = [UNVISITED for _ in range(V)]  # node ids
    low_links = [None for _ in range(V)]  # nodes lowlink values

    # solved = False  # bool value to track if problem is solved or not
    scc_count = 0  # strongly connected node count
    id_curr = 0  # local id variable

    def dfs(at):
        nonlocal id_curr
        nonlocal UNVISITED
        nonlocal scc_count

        stack.append(at)
        onStack[at] = True
        ids[at] = low_links[at] = id_curr
        id_curr += 1

        for to in graph[at]:
            if ids[to] == UNVISITED:
                dfs(to)
            if onStack[to]:
                low_links[at] = min(low_links[at], low_links[to])

        # check if we are at start of strongly connected node
        if ids[at] == low_links[at]:
            while len(stack) > 0:
                node = stack.pop()
                low_links[node] = ids[at]
                onStack[node] = False
                if node == at:
                    break
            scc_count += 1
    
    for at in range(V):
        if ids[at] == UNVISITED:
            dfs(at)
    
    # print(scc_count)
    return scc_count




