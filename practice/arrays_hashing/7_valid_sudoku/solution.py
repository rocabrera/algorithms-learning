"""
https://leetcode.com/problems/valid-sudoku/
----
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        hsblock = {} 
        hscolumn = {} 

        for i, row in enumerate(board):

            hsrow = set() 
            for j, num in enumerate(row):

                if num == '.':
                    continue

                bkey = (i//3, j//3)
                if bkey not in hsblock:
                    hsblock[bkey] = set() 
                elif num in hsblock[bkey]:
                    return False

                if j not in hscolumn:
                    hscolumn[j] = set() 
                elif num in hscolumn[j]:
                    return False

                if num in hsrow:
                    return False

                hsblock[bkey].add(num)
                hscolumn[j].add(num)
                hsrow.add(num)

        return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

Solution().isValidSudoku(board)