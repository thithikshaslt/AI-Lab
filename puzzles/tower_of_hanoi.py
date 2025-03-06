from collections import deque

def is_valid_move(from_rod, to_rod):
    if not from_rod:
        return False
    if not to_rod or from_rod[-1] < to_rod[-1]:
        return True
    return False

def move_disk(state, from_idx, to_idx):
    new_state = [list(rod) for rod in state]
    disk = new_state[from_idx].pop()
    new_state[to_idx].append(disk)
    return tuple(tuple(rod) for rod in new_state)

def bfs(n):
    initial_state = (tuple(range(n, 0, -1)), tuple(), tuple())
    goal_state = (tuple(), tuple(), tuple(range(n, 0, -1)))

    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state)
    parent = {initial_state: None}

    while queue:
        curr = queue.popleft()
        if curr == goal_state:
            path = []
            while curr:
                path.append(curr)
                curr = parent[curr]
            return path[::-1]

        for from_idx in range(3):
            for to_idx in range(3):
                if from_idx != to_idx and is_valid_move(curr[from_idx], curr[to_idx]):
                    new_state = move_disk(curr, from_idx, to_idx)
                    if new_state not in visited:
                        visited.add(new_state)
                        parent[new_state] = curr
                        queue.append(new_state)

sol = bfs(3)

for i, state in enumerate(sol):
    print(f"Step {i}: {state}")
