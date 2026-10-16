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

def dls(state, limit, path, visited):
    if state == goal:
        return path

    if limit == 0:
        return None

    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            visited.add(neighbor)

            result = dls(
                neighbor,
                limit - 1,
                path + [neighbor],
                visited
            )

            if result is not None:
                return result

            visited.remove(neighbor)

    return None

def ids(start, max_depth=50):
    for depth in range(max_depth + 1):
        print("Searching at depth:", depth)

        result = dls(
            start,
            depth,
            [start],
            {start}
        )

        if result is not None:
            print("\nSolution found!")
            print("Number of moves:", len(result) - 1)

            for step, state in enumerate(result):
                print("\nStep", step)

                for i in range(0, 9, 3):
                    print(state[i:i + 3])

            return

    print("No solution found within the maximum depth.")

start = tuple(
    map(int, input("Enter 9 numbers (use 0 for blank): ").split())
)

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input! Enter each number from 0 to 8 exactly once.")
else:
    ids(start)