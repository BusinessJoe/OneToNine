
from dlxsudoku.algorithm_x import algorithm_x
from dlxsudoku.sudoku import Sudoku6x6


if __name__ == "__main__":
    grid = [
        [None, None, None, None, None, 6],
        [None, None, 2, 4, None, None],
        [None, 1, None, 6, 4, None],
        [None, 6, 4, None, 5, None],
        [None, None, 6, 3, None, None],
        [3, None, None, None, None, None]
    ]
    sudoku = Sudoku6x6(grid)

    print(sudoku)
    print()

    matrix = sudoku.to_matrix()
    solutions = algorithm_x(matrix)

    for solution in solutions:
        solved_sudoku = Sudoku6x6.from_algorithm_x_solution(solutions[0])
        print(solved_sudoku)
        print()