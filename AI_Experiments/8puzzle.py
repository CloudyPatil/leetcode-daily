import heapq

goal_state = [1,2,3,4,5,6,7,8,0]

def heuristic(state):
    distance = 0
    for i in range(1,9):
        idx = state.index(i)
        goal_idx = goal_state.index(i)
        x1, y1 = divmod(idx, 3)
        x2, y2 = divmod(goal_idx, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    x, y = divmod(idx, 3)

    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_idx = nx*3 + ny
            new_state = state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(new_state)
    return neighbors

def a_star(start):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {tuple(start): 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal_state:
            path = []
            while tuple(current) in came_from:
                path.append(current)
                current = came_from[tuple(current)]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(current):
            tentative_g = g_score[tuple(current)] + 1

            if tuple(neighbor) not in g_score or tentative_g < g_score[tuple(neighbor)]:
                came_from[tuple(neighbor)] = current
                g_score[tuple(neighbor)] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(open_list, (f_score, neighbor))

    return None

print("Enter the start state (use space between numbers, use 0 for blank):")
print("Example: 1 2 3 4 0 6 7 5 8")

start_state = list(map(int, input().split()))

if len(start_state) != 9:
    print("Invalid input! Please enter exactly 9 numbers.")
else:
    solution = a_star(start_state)

    if solution:
        
        for step in solution:
            for i in range(0,9,3):
                print(step[i:i+3])
            print()
        print("\nSolution found in", len(solution)-1, "moves:\n")
            
    else:
        print("No solution found")
