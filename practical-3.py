import math

MAX_PLAYER, MIN_PLAYER, EMPTY = "X", "O", "_"


class TicTacToe:
    def __init__(self, board: list[list[str]]):
        # initialized empty board.
        self.board = board

    def moves_left(self, board) -> bool:
        # returns true if any open slots are available
        # on the board
        return any(EMPTY in row for row in board)

    def evaluate(self, board):
        lines = [
            *[[(i, j) for j in range(3)] for i in range(3)],  # Rows
            *[[(j, i) for j in range(3)] for i in range(3)],  # Columns
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],  # Diagonals
        ]
        for line in lines:
            a, b, c = line
            if (
                board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]]
                and board[a[0]][a[1]] != EMPTY
            ):
                return 10 if board[a[0]][a[1]] == MAX_PLAYER else -10
        return 0

    def minimax(self, board, depth, is_max, alpha=-math.inf, beta=math.inf):
        score = self.evaluate(board)
        if score:
            return (score - depth) if is_max else (score + depth)
        if not self.moves_left(board):
            return 0

        best = -math.inf if is_max else math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] != EMPTY:
                    continue
                board[i][j] = MAX_PLAYER if is_max else MIN_PLAYER
                val = self.minimax(board, depth + 1, not is_max, alpha, beta)
                board[i][j] = EMPTY
                best = max(best, val) if is_max else min(best, val)
                alpha, beta = (
                    (max(alpha, best), beta) if is_max else (alpha, min(beta, best))
                )
                if alpha >= beta:
                    break
        return best

    def find_best_move(self) -> tuple[int, int]:
        best = (-math.inf, (-1, -1))
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != EMPTY:
                    continue
                self.board[i][j] = MAX_PLAYER
                val = self.minimax(self.board, 0, False)
                self.board[i][j] = EMPTY
                best = max(best, (val, (i, j)), key=lambda x: x[0])
        return best[1]

    def print(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)


# fmt: off
game = TicTacToe(
    [["X", "O", "X"], 
     ["O", "O", "_"], 
     ["_", "_", "X"]]
)
# fmt: on

print("Current board:")
game.print()
print(f"\nThe best move for 'X' is: {game.find_best_move()}")
