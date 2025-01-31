def dls(graph, start, depth, visited=None):
    if visited is None:
        visited = set()

    if depth < 0:
        return
    
    print(start, end=" ")
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dls(graph, neighbor, depth-1, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("\nBFS Traversal:")
dls(graph, 'A',2)
