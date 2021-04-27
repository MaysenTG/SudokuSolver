# SudokuSolver
This Sudoku Solver uses recursive backtracking to quickly compute a sudoku. A basic animation is used to show the answers


The main file for this app is SudokuApp.py. 
- SudokuApp.py controls the pygame commands such as pressing keys and updating the GUI. Only run this file to run the program. Press e to solve an easy puzzle and h to solve a hard puzzle.
- SudokuIO.py is a file which takes the contents from the text file sudoku, and processes it for the program to use
- Solver.py is the file which contains the recursive backtracking algorithm to find the correct number for each cell. The Solver() function searches each cell which is unoccupied, checks whether the numbers 1-9 can go there, and if it can, will insert the number. The function will then be recursively called until it returns true - when all cells are occupied. In this Solver function, a helper function is called, "solveSingletons" which finds cells which can only hold one number and when this number is found, inserts it into the cell.
- Snapshot.py is a file which allows the viewing and manipulation of cells in the snapshot. This file can update, view and clone the snapshot.
- Cell.py is a file which aids in viewing the values of each cell.


Each Sudoku is represented in a text file in the following format:

1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9

Where each number represents the cell. An empty cell is represented by 0

The SudokuApp.py file handles choosing the file. Update this as needed. Otherwise, place all easy sudokus in a file "easypuzzles" and hard in a file "hardpuzzles"
