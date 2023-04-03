#!/usr/bin/python3
import sys

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):
        for r, c in board:
            if col == c or row + col == r + c or row - col == r - c:
                return False
        return True

    def backtrack(board, row, n, result):
        if row == n:
            result.append(board)
            return
        for col in range(n):
            if is_valid(board, row, col):
                backtrack(board + [(row, col)], row + 1, n, result)

    result = []
    backtrack([], 0, n, result)
    for board in result:
        print(' '.join(str(c + 1) for _, c in board))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)

