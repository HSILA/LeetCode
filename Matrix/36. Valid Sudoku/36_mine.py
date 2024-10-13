# https://leetcode.com/problems/valid-sudoku/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                box_values = [
                    board[x][y]
                    for x in range(i * 3, (i + 1) * 3)
                    for y in range(j * 3, (j + 1) * 3)
                    if board[x][y] != "."
                ]
                if len(set(box_values)) != len(box_values):
                    return False

        for k in range(9):
            rows = [board[k][i] for i in range(9) if board[k][i] != "."]
            cols = [board[j][k] for j in range(9) if board[j][k] != "."]

            if len(set(rows)) != len(rows) or len(set(cols)) != len(cols):
                return False

        return True
