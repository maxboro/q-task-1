"""
Counts number of islands for matrix provided using depth-first search (recursive implementation).

Cell considered to be part of island if it has island's cell as neighbour (up, down, left, 
right, but not diagonal neighbour). Time complexity: O(number of cells * number of rows), because 
script visit each cell of matrix only once (in terms of fully processing cell; visit and check if 
it is visited can be done multiple times).


Usage
-----
1. Set shape of matrix in form of '{number of rows} {number of cells}' after "Set shape of matrix:"
2. Set matrix after "Set matrix:". Cells in a row should be separated by 1 whitespace, each new 
row should start at a new line (hit Enter, or insert previously copied multiline matrix altogether).


Example
-------
$ python islands.py
Set shape of matrix: 3 4
Set matrix:
0 0 0 1
0 0 1 1
0 1 0 1
Provided matrix has 2 islands.
"""
from typing import List


def get_matrix() -> List[List[int]]:
    """Receive and process input matrix shape and matrix itself."""
    n_rows, _ = map(int, input('Set shape of matrix: ').split())
    print('Set matrix: ')
    return [list(map(int, input().split())) for _ in range(n_rows)]


def count_islands(matrix: List[List[int]]) -> int:
    """Count number of islands for a given matrix."""

    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def dfs(r: int, c: int) -> None:
        """Perform iteration of depth first search."""

        # If out of bounds, or it's ocean, or already visited, return
        if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] == 0 or visited[r][c]:
            return
        
        # Mark the cell as visited
        visited[r][c] = True

        # Visit all 4 possible directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    
    island_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                # Initiate DFS when found a new island
                dfs(i, j)
                island_count += 1

    return island_count


if __name__ == "__main__":
    matrix = get_matrix()
    n_islands = count_islands(matrix)
    print(f"Provided matrix has {n_islands} islands.")
