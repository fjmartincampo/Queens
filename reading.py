def readdimensions():

    # Ask the user for the dimensions of the chessboard
    while True:
        try:
            rows = int(input("Number of rows: "))
            columns = int(input("Number of columns: "))

            if rows <= 0 or columns <= 0:
                print("Both dimensions must be positive integers.\n")
                continue

            return rows, columns

        except ValueError:
            print("Please enter valid integers.\n")