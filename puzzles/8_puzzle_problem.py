from collections import deque

def is_solvable(state):
    flat_state = [num for row in state for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1
    return inversions % 2 == 0

# Function to generate neighbors of a given state
def generate_neighbors(state):

    neighbors = []

    # to find the tile with 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row, zero_col = i, j #store the indices of 0 tile
                break

    # possible moves
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dr, dc in moves:
        # new indices of 0 tile
        new_r, new_c = zero_row + dr, zero_col + dc

        # new index must be within the bounds
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            new_state = [row[:] for row in state]

            # generating new state by swapping
            new_state[zero_row][zero_col], new_state[new_r][new_c] = (
                new_state[new_r][new_c], new_state[zero_row][zero_col]
            )
            
            # append to list
            neighbors.append(new_state)

    return neighbors

initial_state = [
    [1, 2, 7],
    [8, 0, 3],
    [6, 4, 5]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

if not is_solvable(initial_state):
    print("This puzzle is unsolvable.")
else:
    # BFS queue
    queue = deque()
    queue.append(initial_state)

    # keep track of states that were explored
    seen = set()
    seen.add(tuple(map(tuple, initial_state)))

    steps = 0

    while queue:
        steps += 1
        curr_state = queue.popleft()

        if curr_state == goal_state:
            print(f"Goal reached in {steps} steps!")
            break

        neighbors = generate_neighbors(curr_state)
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor)) not in seen:
                queue.append(neighbor)
                seen.add(tuple(map(tuple, neighbor)))