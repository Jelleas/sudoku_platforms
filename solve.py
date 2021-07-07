import argparse
import os
import sys

from sudoku import load_from_file

def solve(sudoku):
    stack = [sudoku]

    while stack:
        sudoku = stack.pop()

        if sudoku.is_solved():
            return sudoku

        x, y = sudoku.next_empty_index()
        
        for option in sudoku.options_at(x, y):
            child_sudoku = sudoku.copy()
            child_sudoku.place(option, x, y)
            stack.append(child_sudoku)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve a sudoku puzzle.')

    parser.add_argument("puzzle", type=int, help="identifier of the puzzle to be solved")
    parser.add_argument("-n", type=int, default=1, dest="number_of_runs", help="number of runs")

    args = parser.parse_args()

    puzzle_path = f"puzzles/{args.puzzle}.csv"

    if not os.path.exists(puzzle_path):
        print(f"puzzle {args.puzzle} does not exist")
        sys.exit(1)

    sudoku = load_from_file(puzzle_path)

    print(sudoku)
    print()
    print("SOLVING...")

    for i in range(args.number_of_runs):
        solved_sudoku = solve(sudoku)

    print("DONE SOLVING")
    print()
    print(solved_sudoku)