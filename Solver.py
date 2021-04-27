# Solver 2021
# Template for the algorithm to solve a sudoku. Builds a recursive backtracking solution
# that branches on possible values that could be placed in the next empty cell. 
# Initial pruning of the recursion tree - 
#       we don't continue on any branch that has already produced an inconsistent solution
#       we stop and return a complete solution once one has been found
import Cell
import Sudoku_IO
import pygame


def number_unassigned(row, col, matrix):
    num_unassign = 0
    for i in range(0, 10):
        for j in range(0, 3):
            # cell is unassigned
            if matrix[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a


def solve(snapshot, screen):
    # display current snapshot
    pygame.time.delay(75)
    Sudoku_IO.displayPuzzle(snapshot, screen)
    pygame.display.flip()

    # List of  all unsolved cells
    lst = snapshot.unsolvedCells()

    # Function returns True, puzzle is complete
    if isComplete(snapshot):
        return True
    else:
        row = lst[0].getRow()
        col = lst[0].getCol()

    if solveSingletons(snapshot):
        # Loops through the possible numbers and tries them in the cell, if it
        for num in range(1, 10):
            # Checks if the number is able to fit into the current cell (in the row, col and block)
            if checkConsistency(snapshot, num, row, col):
                snapshot.setCellVal(row, col, num)

                # Recursively call the function and if its solved, return true
                if solve(snapshot, screen):
                    return True

            snapshot.setCellVal(row, col, 0)
        return False


def solveSingletons(snapshot):
    possible_nums = []
    lst = snapshot.unsolvedCells()

    # If the sudoku is complete, end the function
    if isComplete(snapshot):
        return True
    else:
        # Set the start row and col to the first unassigned value
        row = lst[0].getRow()
        col = lst[0].getCol()

    for singletons in range(1, 10):
        if checkConsistency(snapshot, singletons, row, col):
            possible_nums.append(singletons)

            # Have we found a singleton? If so, great! Use that number in the cell and reset the array
            if len(possible_nums) == 1:
                snapshot.setCellVal(row, col, possible_nums[0])
                possible_nums.clear()

            # If our singleton solving function is finished, return  true
            if solveSingletons(snapshot):
                return True
        # If there's no value, move onto the next cell.
        snapshot.setCellVal(row, col, 0)
    return False


# Check whether a snapshot is consistent, i.e. all cell values comply 
# with the sudoku rules (each number occurs only once in each block, row and column).
def checkConsistency(snapshot, num, row, col):
    # Simpler way of checking number in row
    if num in [rows.getVal() for rows in snapshot.cellsByRow(row)]:
        return False

    # Simpler way of checking number in col
    if num in [cols.getVal() for cols in snapshot.cellsByCol(col)]:
        return False

    # Simpler way of checking for nums in block
    if num in [blocks.getVal() for blocks in snapshot.cellsByBlock(row, col)]:
        return False

    return True

# Check whether a puzzle is solved.
# return true if the sudoku is solved, false otherwise
def isComplete(snapshot):
    if len(snapshot.unsolvedCells()) == 0:  # If unsolved array is empty, then all cells have been used and it is solved
        return True
    else:
        return False
