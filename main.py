from reading import readdimensions
from model import solve
from printing import printboard


def main():

    print("Maximum Non-Attacking Queens Problem")
    print("------------------------------------")

    rows, columns = readdimensions()

    board = solve(rows, columns)

    print("\nOptimal solution:\n")
    printboard(board)


if __name__ == "__main__":
    main()