from dls import dls

def ids(graph, start, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        print(f"\ndepth: {depth}")
        dls(graph, start, depth, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("\nIterative Deepening Search:")
ids(graph, 'A', 3)

