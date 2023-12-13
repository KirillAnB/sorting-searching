

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            neigbors = graph[node]
            for neighbor in neigbors:
                queue.append(neighbor)
    return visited
my_graph = {
    'node1':{'node2', 'node3', 'node4'},
    'node2':{'node1'},
    'node3':{'node1'},
    'node4':{'node1', 'node5'},
    'node5':{'node4'}
}
print(bfs(my_graph, 'node1'))
def dfs(graphh, start_node, visited = None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    print(start_node)
    for next_node in graphh[start_node] - visited:
        dfs(graphh, next_node, visited)
    return visited



graph = {
    'Amin': {"Vasim", "Nick", "Mike"},
    'Vasim': {"Imram", 'Amin'},
    'Imram': {"Vasim", 'Faras'},
    'Faras': {'Imram'},
    'Mike': {'Amin'},
    'Nick': {'Amin'}
}

print(bfs(graph, 'Vasim'))
print(dfs(my_graph, 'node1'))
