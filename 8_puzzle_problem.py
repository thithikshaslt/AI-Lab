from collections import deque

def generate_neighbors(state):
    neighbors=[]

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_row, zero_col = i, j
                break

    moves = [
        (0,1),  #Right
        (0,-1), #Left
        (1,0),  #Down
        (-1,0)  #Up
    ]

    
initial_state = [
    [1,2,3],
    [0,4,6],
    [5,7,8]
]

goal_state = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

queue = deque()
queue.append([initial_state])

seen = set()

while queue:
    curr_state = queue.popleft()

    if curr_state == goal_state:
        print("Goal reached!")
        break

    neighbors = generate_neighbors(current_state)

    for neighbor in neighbors:
        if neighbor not in seen:
            queue.append(neighbor)
            seen.add(neighbor)



