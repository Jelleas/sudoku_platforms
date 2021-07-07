## Installation

```
pip install -r requirements.txt
```

## How to run

```
$ python solve.py -h
usage: solve.py [-h] [-n NUMBER_OF_RUNS] puzzle

Solve a sudoku puzzle.

positional arguments:
  puzzle             identifier of the puzzle to be solved

optional arguments:
  -h, --help         show this help message and exit
  -n NUMBER_OF_RUNS  number of runs
```

For instance, to solve the fourth puzzle ten times, run:

```
python solve.py -n 10 4
```

## Testing

To test the implementation simply run `pytest` in the root folder of the project.

```
pytest
```

> if the pytest command fails, do make sure all required dependencies are installed via `pip install -r requirements.txt`. Alternatively, if the pytest command is not found, try `python -m pytest` instead.

## Profiling

To create a profile run:

```
python -m cProfile -o solve.prof solve.py -n 10 4
```

This creates a file called `solve.prof` that can then be inspected through:

```
snakeviz solve.prof
```

> if the snakeviz command fails, do make sure all required dependencies are installed via `pip install -r requirements.txt`. Alternatively, if the snakeviz command is not found, try `python -m snakeviz solve.prof` instead.