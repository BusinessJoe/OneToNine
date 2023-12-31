import time
from rules.antiknight import AntiKnight9x9
from rules.standard import StandardBox, Col, Row
from sudoku import Sudoku


def add_rows(row1, row2):
    return [x1 + x2 for x1, x2 in zip(row1, row2)]


if __name__ == "__main__":
    # grid = [
    #     [None, 1, None, None, 5, None, None, None, None],
    #     [3, None, None, None, None, 7, 2, None, 6],
    #     [None, None, None, None, 1, 6, None, None, 7],
    #     [4, None, None, None, 6, None, None, None, None],
    #     [None, None, None, None, None, 3, 9, None, 5],
    #     [None, 3, 9, None, None, 1, None, 2, None],
    #     [8, None, 4, None, None, None, None, 6, None],
    #     [None, 7, None, None, None, None, None, None, None],
    #     [6, None, None, None, None, None, None, 5, 9],
    # ]
    # grid = [
    #     [5, 8, None, None, 6, 7, 2, None, None],
    #     [None, None, None, 9, 8, 2, 5, 7, 1],
    #     [2, None, 1, None, None, None, 9, None, None],
    #     [None, 9, None, 2, None, 4, 7, None, 8],
    #     [7, 3, None, None, None, None, None, 2, 5],
    #     [None, 1, 2, 8, 7, None, None, None, 9],
    #     [1, None, 7, 5, None, None, 8, None, None],
    #     [None, None, 6, None, 2, None, None, 4, 7],
    #     [None, None, 3, None, None, 9, None, None, None],
    # ]
    # grid = [
    #     [6, 3, None, None, None, None, None, 8, 1],
    #     [None, 2, None, None, None, 3, None, None, None],
    #     [None, None, None, None, 1, 7, 4, 3, None],
    #     [None, 9, 6, 4, None, None, 5, 7, None],
    #     [None, None, None, 7, 6, 2, None, None, None],
    #     [None, 8, None, None, None, None, 6, None, None],
    #     [None, 6, None, None, 2, None, None, None, None],
    #     [3, None, 9, None, None, None, None, 6, None],
    #     [None, None, None, None, None, None, None, None, 9],
    # ]
    # sudoku = Sudoku([Row(), Col(), StandardBox()], grid)

    # Anti-knight
    grid = [
        [None, 1, None, None, None, None, None, None, None],
        [None, None, 2, None, None, None, None, None, None],
        [None, None, None, 3, None, None, None, None, None],
        [1, None, None, None, 4, None, None, None, None],
        [None, 7, None, None, None, 5, None, None, None],
        [None, None, 8, None, None, None, 6, None, None],
        [None, None, None, 4, None, None, None, 1, None],
        [None, None, None, None, None, None, None, None, None],
        [9, None, 7, None, None, None, None, None, None],
    ]
    sudoku = Sudoku([Row(), Col(), StandardBox(), AntiKnight9x9()], grid)

    print(sudoku)
    print()

    print("generating dlx graph...")
    start = time.perf_counter_ns()

    graph = sudoku.to_graph()

    end = time.perf_counter_ns()
    print(f"done in {(end - start) // 1000000} ms\n")

    print("starting search...")
    start = time.perf_counter_ns()

    solutions = list(graph.search())

    end = time.perf_counter_ns()
    print(f"done in {(end - start) // 1000000} s\n")

    for solution in solutions:
        solved_sudoku = Sudoku.from_algorithm_x_solution(solution)
        print(solved_sudoku)
        print()
