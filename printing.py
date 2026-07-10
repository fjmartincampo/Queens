# Function to print the chessboard
# Function to print the chessboard
def printboard(board):
    rows = len(board)
    columns = len(board[0])

    # Calculating width for the borders of the chessboard
    width = 2 * columns + 1

    print("+" + "-" * width + "+")

    # Printing the chessboard with 'Q' for queens and '-' for empty spaces
    for i in range(rows):
        print("|", end=" ")
        for j in range(columns):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print("|")

    print("+" + "-" * width + "+")