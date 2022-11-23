import queue

graph_simple = {
'A' : ['B','C'],
'B' : ['A','D', 'E'],
'C' : ['A','F', 'G'],
'D' : ['B','H'],
'E' : ['B','G', 'I'],
'F' : ['C','J'],
'G' : ['C','E','J'],
'H' : ['D'],
'I' : ['E','J'],
'J' : ['F','G','I']
}


def depth_first_search(graph, start):
    stack_nodes = queue.LifoQueue(len(graph))
    visited = set()
    prev_nodes = dict()
    _drop  = set()

    prev_nodes[start] = None
    visited.add(start)
    stack_nodes.put(start)
    found_dest = False

    while(not stack_nodes.empty()):
        node = stack_nodes.get()
        can = True
        for dest in reversed(graph[node]):
            if len(graph[dest]) <=1:
                can = False
            if dest not in visited:
                prev_nodes[dest] = node
                visited.add(dest)
                stack_nodes.put(dest)
        if can:
            _drop.add(node)
    # path = list()
    # if found_dest:
    #     path.append(end)
    #     prev = prev_nodes[end]
    #     while prev is not None:
    #         path.append(prev)
    #         prev = prev_nodes[prev]
    #     path.reverse()
    return _drop

print(depth_first_search(graph_simple, 'A'))