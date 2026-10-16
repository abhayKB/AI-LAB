goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

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

def dfs(start):
    stack = [(start, [start])]
    visited = {start}

    while stack:
        current, path = stack.pop()

        if current == goal:
            print("\nSolution found!")
            print("Number of moves:", len(path) - 1)

            for step, state in enumerate(path):
                print("\nStep", step)

                for i in range(0, 9, 3):
                    print(state[i:i + 3])

            return

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    print("No solution found.")

start = tuple(
    map(int, input("Enter 9 numbers (use 0 for blank): ").split())
)

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input! Enter each number from 0 to 8 exactly once.")
else:
    dfs(start)