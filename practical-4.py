def solve_n_queens(n):
    def is_safe(row, col):
        return (
            col not in cols
            and (row - col) not in neg_diags
            and (row + col) not in pos_diags
        )

    def backtrack(row):
        if row == n:
            board = []
            for r in range(n):
                line = ["."] * n
                line[queens[r]] = "Q"
                board.append("".join(line))
            res.append(board)
            return
        for col in range(n):
            if is_safe(row, col):
                queens[row] = col
                cols.add(col)
                pos_diags.add(row + col)
                neg_diags.add(row - col)
                backtrack(row + 1)
                cols.remove(col)
                pos_diags.remove(row + col)
                neg_diags.remove(row - col)

    res = []
    cols = set()
    pos_diags = set()  # row + col
    neg_diags = set()  # row - col
    queens = [0] * n
    backtrack(0)
    return res


solutions = solve_n_queens(4)
for sol in solutions:
    for row in sol:
        print(row)
    print()


def solve_n_queens_bb(n):
    def solve(row):
        if row == n:
            board = []
            for r in range(n):
                line = ["."] * n
                line[positions[r]] = "Q"
                board.append("".join(line))
            solutions.append(board)
            return

        for col in range(n):
            if (
                not cols[col]
                and not pos_diag[row + col]
                and not neg_diag[row - col + n - 1]
            ):
                # bound check passed, proceed
                positions[row] = col
                cols[col] = True
                pos_diag[row + col] = True
                neg_diag[row - col + n - 1] = True

                solve(row + 1)

                # backtrack
                cols[col] = False
                pos_diag[row + col] = False
                neg_diag[row - col + n - 1] = False

    # initialize tracking arrays
    solutions = []
    cols = [False] * n
    pos_diag = [False] * (2 * n - 1)  # row + col
    neg_diag = [False] * (2 * n - 1)  # row - col + offset
    positions = [0] * n

    solve(0)
    return solutions


print("\n\nBranch and Bound")
# example usage
for sol in solve_n_queens_bb(4):
    for row in sol:
        print(row)
    print()
