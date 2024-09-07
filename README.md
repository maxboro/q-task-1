# Task 1

As part of this task I created script `islands.py` that counts number of islands for matrix provided using depth-first search (recursive implementation).

Cell considered to be part of island if it has island's cell as neighbour (up, down, left, right, but not diagonal neighbour). Time complexity: O(number of cells * number of rows), because script visit each cell of matrix only once (in terms of fully processing cell; visit and check if it is visited can be done multiple times).

## Usage
Created and tested in Python 3.9.13.
1. Run a script:
```bash
$ python islands.py
```
2. Set shape of matrix in form of '{number of rows} {number of cells}' after "Set shape of matrix:"
3. Set matrix after "Set matrix:". Cells in a row should be separated by 1 whitespace, each new row should start at a new line (hit Enter, or insert previously copied multiline matrix altogether).
4. Script would print message: "Provided matrix has [number] islands." with number of islands.

## Example:
```bash
$ python islands.py
```
```text
Set shape of matrix: 3 4
Set matrix:
0 0 0 1
0 0 1 1
0 1 0 1
Provided matrix has 2 islands.
```
