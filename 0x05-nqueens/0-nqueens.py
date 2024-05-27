#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard. Write a
program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number
of arguments, print Usage: nqueens N, followed by a new
line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a
new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a
new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module"""
import sys


def print_usage_and_exit():
    """printing the usage"""
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid_number(n):
    """function that check if the input is valid"""
    try:
        num = int(n)
        return num
    except ValueError:
        return None


def solve_n_queens(N):
    """solve n queens function"""
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col):
        """ function that solve the problem"""
        if col >= N:
            result = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        result.append([i, j])
            solutions.append(result)
            return True
        res = False
        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                res = solve(board, col + 1) or res
                board[i][col] = 0
        return res

    solutions = []
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve(board, 0)
    return solutions


def main():
    """the main function that run the code"""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    n = sys.argv[1]
    N = is_valid_number(n)
    if N is None:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_n_queens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
