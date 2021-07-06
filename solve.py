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


sudoku = load_from_file("hard/puzzle4.sudoku")

print(sudoku)
print()
print("SOLVING...")

solved_sudoku = solve(sudoku)

print("DONE SOLVING")
print()
print(solved_sudoku)