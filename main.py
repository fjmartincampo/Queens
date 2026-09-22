from reading import readdimensions
from model import solve
from printing import printboard

# Maximum Non-Attacking Queens Problem
print("Maximum Non-Attacking Queens Problem")
print("------------------------------------")

# Reading the board dimensions from the user
rows, columns = readdimensions()

# Solving the problem
board = solve(rows, columns)

# Printing the solution
print("\nOptimal solution:\n")
printboard(board)