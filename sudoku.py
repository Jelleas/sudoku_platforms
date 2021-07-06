class Sudoku:
    def __init__(self, puzzle):
        self._grid = []

        for puzzle_row in puzzle:
            row = ""

            for element in puzzle_row:
                row += element
            
            self._grid.append(row)


    def place(self, value, x, y):
        row = self._grid[y]
        new_row = ""

        for i in range(9):
            if i == x:
                new_row += str(value)
            else:
                new_row += row[i]

        self._grid[y] = new_row


    def copy(self):
        return Sudoku(self._grid)


    def value_at(self, x, y):
        row = self._grid[y]
        return int(row[x])


    def options_at(self, x, y):
        options = [1,2,3,4,5,6,7,8,9]

        for value in self.row_values(y):
            if value in options:
                options.remove(value)

        for value in self.column_values(x):
            if value in options:
                options.remove(value)

        block_index = (y // 3) * 3 + x // 3
        for value in self.block_values(block_index):
            if value in options:
                options.remove(value)

        return options
        

    def next_empty_index(self):
        for y in range(9):
            for x in range(9):
                if self.value_at(x, y) == 0:
                    return x, y
        
        return -1, -1


    def row_values(self, i):
        """Returns all values at i-th row."""
        values = []

        for j in range(9):
            values.append(self.value_at(j, i))

        return values


    def column_values(self, i):
        """Returns all values at i-th column."""
        values = []

        for j in range(9):
            values.append(self.value_at(i, j))

        return values


    def block_values(self, index):
        """
        Returns all values at index-th block.
        The blocks are arranged as follows:
        0 1 2
        3 4 5
        6 7 8
        """
        values = []

        x_start = (index % 3) * 3
        y_start = (index // 3) * 3

        for x in range(x_start, x_start + 3):
            for y in range(y_start, y_start + 3):
                values.append(self.value_at(x, y))

        return values        


    def is_solved(self):
        """
        Returns True if and only if all rows, columns and blocks contain
        only the numbers 1 through 9. False otherwise.
        """
        values = [1,2,3,4,5,6,7,8,9]

        for i in range(9):
            for value in values:
                if value not in self.column_values(i):
                    return False

                if value not in self.column_values(i):
                    return False

                if value not in self.block_values(i):
                    return False

        return True


    def __str__(self):
        representation = ""

        for row in self._grid:
            representation += row + "\n"
        
        return representation.strip()


def load_from_file(filename):
    puzzle = []

    with open(filename) as f:
        for line in f:
            
            # strip newline and remove all commas
            line = line.strip().replace(",", "")

            puzzle.append(line)

    return Sudoku(puzzle)