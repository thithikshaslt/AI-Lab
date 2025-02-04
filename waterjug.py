# using bfs 

from collections import deque

def jug(x,y,target):
    initial_state = (0,0)

    if target > max(x,y):
        return "Target can never be achieved"
    
    queue = deque([initial_state])

    visited = set()
    visited.add(initial_state)

    parent={}

    while queue:
        curr = queue.popleft()
        jug1,jug2 = curr

        if jug1 == target or jug2 ==target:
            path=[]
            while curr != initial_state:
                path.append(curr)
                curr = parent[curr]
            path.append(initial_state)
            return path[::-1]
        
        next_states = [
            (x,jug2),
            (jug1,y),
            (0,jug2),
            (jug1,0),
            (max(0, jug1-(y-jug2)), min(y,jug2+jug1)),
            (min(x,jug1+jug2), max(0,jug2-(x-jug1)))

        ]

        for next in next_states:
            if next not in visited:
                visited.add(next)
                parent[next] = curr
                queue.append(next)

    return "No solution"

x = 7  
y = 3  
target = 5 

solution = jug(x, y, target)
print("Solution path:", solution)
