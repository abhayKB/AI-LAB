import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = (
                new_state[new_zero],
                new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors

def astar(start):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start), 0, start))

    parent = {start: None}
    cost = {start: 0}

    while priority_queue:
        f, g, current = heapq.heappop(priority_queue)

        if g != cost[current]:
            continue

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("\nSolution found!")
            print("Number of moves:", len(path) - 1)

            for step, state in enumerate(path):
                print("\nStep", step)

                for i in range(0, 9, 3):
                    print(state[i:i + 3])

            return

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if neighbor not in cost or new_g < cost[neighbor]:
                cost[neighbor] = new_g
                parent[neighbor] = current

                h = heuristic(neighbor)
                new_f = new_g + h

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor)
                )

    print("No solution found.")

start = tuple(
    map(int, input("Enter 9 numbers (use 0 for blank): ").split())
)

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input! Enter each number from 0 to 8 exactly once.")
else:
    astar(start)