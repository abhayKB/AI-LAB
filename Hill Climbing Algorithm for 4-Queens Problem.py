import random

N = 4

def calculate_cost(board):
    conflicts = 0

    for col1 in range(N):
        for col2 in range(col1 + 1, N):
            row1 = board[col1]
            row2 = board[col2]

            if row1 == row2 or abs(row1 - row2) == abs(col1 - col2):
                conflicts += 1

    return conflicts

def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def get_neighbors(board):
    neighbors = []

    for col in range(N):
        for row in range(N):
            if row != board[col]:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append(new_board)

    return neighbors

def hill_climbing():
    attempts = 0

    while True:
        attempts += 1

        current = [random.randint(0, N - 1) for _ in range(N)]

        print("\nInitial board:")
        print_board(current)
        print("Initial cost:", calculate_cost(current))

        while True:
            current_cost = calculate_cost(current)

            if current_cost == 0:
                print("\nGoal configuration reached!")
                print("Final board:")
                print_board(current)
                print("Final cost:", current_cost)
                print("Attempts:", attempts)
                return

            neighbors = get_neighbors(current)

            best_neighbor = min(neighbors, key=calculate_cost)
            best_cost = calculate_cost(best_neighbor)

            print("\nCurrent state:", current)
            print("Current cost:", current_cost)
            print("Best neighbor:", best_neighbor)
            print("Neighbor cost:", best_cost)

            if best_cost < current_cost:
                current = best_neighbor
                print("Moving to better neighbor...")
            else:
                print("Local minimum reached. Restarting..." )
                break

hill_climbing()