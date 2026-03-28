import heapq

goal = [1,2,3,4,5,6,7,8,0]

# Heuristic: misplaced tiles
def heuristic(state):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

# Print puzzle nicely
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Get neighbors
def get_neighbors(state):
    neighbors = []
    i = state.index(0)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    x, y = divmod(i, 3)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = state[:]
            ni = nx * 3 + ny
            new_state[i], new_state[ni] = new_state[ni], new_state[i]
            neighbors.append(new_state)

    return neighbors

# A* algorithm with path tracking
def astar(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))

        # Add current state to path
        path = path + [state]

        if state == goal:
            print("\n✅ Solution Found!\n")
            print("Steps:", len(path) - 1)
            print("\nPath:\n")

            for step in path:
                print_state(step)

            return

        for neighbor in get_neighbors(state):
            heapq.heappush(pq, (g + 1 + heuristic(neighbor), g + 1, neighbor, path))

    print("❌ No solution found")

# Input with validation
while True:
    try:
        start = list(map(int, input("Enter 9 numbers (0-8): ").split()))
        if len(start) != 9 or set(start) != set(range(9)):
            print("❌ Invalid input, try again")
            continue 
        break
    except:
        print("❌ Invalid input")

astar(start)