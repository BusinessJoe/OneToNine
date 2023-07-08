class Matrix:
    rows: list[bool]
    columns: list[bool]
    A: list[list[bool]]

    def __init__(self, A: list[list[bool]], rows = None, columns = None) -> None:
        self.rows = [True] * len(A) if rows is None else rows
        self.columns = [True] * len(A[0]) if columns is None else columns
        self.A = A

    def is_empty(self) -> bool:
        if not any(self.columns):
            return True
        return False
    
    def choose_column(self) -> int:
        # Raises ValueError if no columns exist
        least_trues = None
        for idx, val in enumerate(self.columns):
            if not val:
                continue
        
            if least_trues is None:
                least_trues = (idx, self._count_true(idx))
            elif self._count_true(idx) < least_trues[1]:
                least_trues = (idx, self._count_true(idx))

        if least_trues is not None:
            return least_trues[0]
        
        raise ValueError("no columns found")
    
    
    def _count_true(self, col_idx):
        row_idxs = [idx for idx, val in enumerate(self.rows) if val]
        count = 0
        for row in row_idxs:
            if self.A[row][col_idx]:
                count += 1
        return count
    
    def list_rows(self, col_idx) -> list[int]:
        indices = [idx for idx, val in enumerate(self.rows) if val and self.A[idx][col_idx]]
        return indices
    
    def del_col(self, col_idx):
        self.columns[col_idx] = False

    def del_row(self, row_idx):
        self.rows[row_idx] = False

    def copy(self):
        return Matrix(self.A, self.rows.copy(), self.columns.copy())

    def __str__(self) -> str:
        display_list = []

        for row_idx, row in enumerate(self.A):
            if not self.rows[row_idx]:
                continue

            display_row = []
            for col_idx, val in enumerate(row):
                if not self.columns[col_idx]:
                    continue

                display_row.append("1" if self.A[row_idx][col_idx] else "0")
            display_list.append(" ".join(display_row))
        return "\n".join(display_list)


def algorithm_x(matrix: Matrix, partial_solution = None, level: int = 0):
    if partial_solution is None:
        partial_solution = []

    if matrix.is_empty():
        return [partial_solution]

    solutions = []

    col_choice = matrix.choose_column()
    for row_choice in matrix.list_rows(col_choice):
        partial_solution = partial_solution.copy()

        old_columns = matrix.columns.copy()
        old_rows = matrix.rows.copy()

        for j in range(len(matrix.columns)):
            if not matrix.columns[j] or not matrix.A[row_choice][j]:
                continue

            for i in range(len(matrix.rows)):
                if not matrix.rows[i] or not matrix.A[i][j]:
                    continue

            
                matrix.del_row(i)
            
            matrix.del_col(j)

        solutions.extend(algorithm_x(matrix, partial_solution + [row_choice], level + 1))

        matrix.columns = old_columns
        matrix.rows = old_rows

    return solutions

if __name__ == "__main__":
    A = [
        [1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 1]
    ]

    matrix = Matrix(A)

    for solution in algorithm_x(matrix):
        print(solution)