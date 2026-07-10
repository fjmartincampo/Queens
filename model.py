from gurobipy import *

def solve(rows, columns):
    
    # Defining the model
    model = Model("MaximumQueens")

    # Decision variables
    x = {}
    for i in range(rows):
        for j in range(columns):
            x[i, j] = model.addVar(vtype=GRB.BINARY, name=f"x_{i}_{j}")

    # Objective function: maximize the number of queens placed on the board
    model.setObjective(quicksum(x[i, j] for i in range(rows) for j in range(columns)), GRB.MAXIMIZE)

    # One queen at most per row
    for i in range(rows):
        model.addConstr(quicksum(x[i, j] for j in range(columns)) <= 1)

    # One queen at most per column
    for j in range(columns):
        model.addConstr(quicksum(x[i, j] for i in range(rows)) <= 1)

    # One queen at most per diagonal \
    for d in range(-(rows - 1), columns):
        cells = [(i, j) for i in range(rows) for j in range(columns) if j - i == d]

        if len(cells) > 1:
            model.addConstr(quicksum(x[i, j] for i, j in cells) <= 1)

    # One queen at most per diagonal /
    for s in range(rows + columns - 1):
        cells = [(i, j) for i in range(rows) for j in range(columns) if i + j == s]

        if len(cells) > 1:
            model.addConstr(quicksum(x[i, j] for i, j in cells) <= 1)

    # Hide Gurobi output and optimize the model
    model.Params.OutputFlag = 0
    model.optimize()

    board = [[0 for _ in range(columns)] for _ in range(rows)]

    if model.Status == GRB.OPTIMAL:
        for i in range(rows):
            for j in range(columns):
                if x[i, j].X > 0.5:
                    board[i][j] = 1

    return board