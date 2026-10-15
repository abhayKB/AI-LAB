# Tic Tac Toe

empty_box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
X = []
O = []

winning_sets = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]


def display_board():
    for i in range(1, 10):

        if i in X:
            print("X", end=" ")
        elif i in O:
            print("O", end=" ")
        else:
            print(i, end=" ")

        if i % 3 == 0:
            print()


def check_win(player):
    for combination in winning_sets:

        if all(position in player for position in combination):
            return True

    return False


player = "X"

while len(empty_box) > 0:

    display_board()

    print("\nAvailable boxes:", empty_box)

    position = int(input(f"Player {player}, enter your position: "))

    # Check if position is valid
    if position not in empty_box:
        print("Invalid move! Choose an available box.")
        continue

    # Remove from empty boxes
    empty_box.remove(position)

    # Add position to player's list
    if player == "X":
        X.append(position)

        # Check if X wins
        if check_win(X):
            display_board()
            print("\nX Wins!")
            break

        player = "O"

    else:
        O.append(position)

        # Check if O wins
        if check_win(O):
            display_board()
            print("\nO Wins!")
            break

        player = "X"

else:
    display_board()
    print("\nIt's a Draw!")

print("\nX positions:", X)
print("O positions:", O)