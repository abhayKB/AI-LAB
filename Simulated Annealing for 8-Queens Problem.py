import random
import math

N = 8

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


def get_neighbor(board):
    neighbor = board.copy()

    col = random.randint(0, N - 1)

    new_row = random.randint(0, N - 1)

    while new_row == neighbor[col]:
        new_row = random.randint(0, N - 1)

    neighbor[col] = new_row

    return neighbor


def simulated_annealing():
    current = [random.randint(0, N - 1) for _ in range(N)]

    temperature = 100.0
    cooling_rate = 0.995
    max_iterations = 100000

    current_cost = calculate_cost(current)
    best = current.copy()
    best_cost = current_cost

    print("Initial board:")
    print_board(current)
    print("Initial cost:", current_cost)

    for iteration in range(1, max_iterations + 1):

        if current_cost == 0:
            break

        neighbor = get_neighbor(current)
        neighbor_cost = calculate_cost(neighbor)

        delta = neighbor_cost - current_cost

        if delta < 0:
            current = neighbor
            current_cost = neighbor_cost

        elif random.random() < math.exp(-delta / temperature):
            current = neighbor
            current_cost = neighbor_cost

        if current_cost < best_cost:
            best = current.copy()
            best_cost = current_cost

        temperature *= cooling_rate

        if temperature < 1e-10:
            temperature = 1e-10

    print("\nFinal board:")
    print_board(best)

    print("Final cost:", best_cost)
    print("Iterations:", iteration if 'iteration' in locals() else 0)

    if best_cost == 0:
        print("Solution found!")
    else:
        print("No solution found in this run. Try running again.")

simulated_annealing()