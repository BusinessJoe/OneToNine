from __future__ import annotations

from typing import Self
from dlx import DlxGraph

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from rules import Rule


class Sudoku:
    grid: list[list[int | None]]
    rules: list[Rule]
    num_rows = 9
    num_cols = 9
    max_val = 9

    def __init__(self, rules, grid) -> None:
        self.grid = grid
        self.rules = rules

    def to_graph(self) -> DlxGraph:
        """
        Rows of the graph are in the order
        R1C1#1, R1C1#2, ..., R1C2#1, R1C2#2, ...
        """

        matrix = self._row_column_constraints()

        for r in self.rules:
            constraints = r.dlx_constraints(self)
            matrix.extend(constraints)

        matrix_transpose = [list(i) for i in zip(*matrix)]
        return DlxGraph(matrix_transpose)

    def _matrix_row_idx(self, row: int, col: int, val: int) -> int:
        return row * 81 + col * 9 + val

    def _row_column_constraints(self) -> list[list[bool]]:
        constraints = []
        for row in range(9):
            for col in range(9):
                constraint = [False] * 9 * 9 * 9

                if self.grid[row][col] is None:
                    for val in range(9):
                        constraint[self._matrix_row_idx(row, col, val)] = True
                else:
                    constraint[
                        self._matrix_row_idx(row, col, self.grid[row][col] - 1)
                    ] = True

                constraints.append(constraint)

        return constraints

    @classmethod
    def from_algorithm_x_solution(cls, solution: list[int]) -> Self:
        grid = [[None] * 9 for _ in range(9)]

        for solution_row in solution:
            row, col, val = cls._algorithm_x_solution_row_to_grid_value(solution_row)
            grid[row][col] = val + 1

        return cls([], grid)

    @staticmethod
    def _algorithm_x_solution_row_to_grid_value(solution_row) -> tuple[int, int, int]:
        val = solution_row % 9
        col = solution_row // 9 % 9
        row = solution_row // (9 * 9)

        return row, col, val

    def __str__(self) -> str:
        display_list = []
        for row in self.grid:
            string_nums = [str(x) if x is not None else "_" for x in row]
            string_nums[6:6] = "|"
            string_nums[3:3] = "|"
            display_list.append(" ".join(string_nums))

        display_list[6:6] = ["-" * 21]
        display_list[3:3] = ["-" * 21]
        return "\n".join(display_list)
