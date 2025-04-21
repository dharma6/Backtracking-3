'''
TC: O(n*n!)*
SC: O(n*n)+O(n) --> Board+ Recursive stack space

As stated, it is a hard problem,I took good amount of time to solve it.

Close to 2 hours, after seeing the solution taught by the instructor.

Major mistakes performed are

1. Understanding the base case, that you return the control, when the rows reached the n, as in the grid, we only traverse through n-1.

2. And also returning the control, if you are not able to fill the Queen in the second for loop.

3. Retrieving the information from the grid in the format which output requires.

'''

import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        final_res = []

        matrix_fill = [["." for i in range(n)] for j in range(n)]
        self.helper(matrix_fill, 0, n, res)

        for i in range(len(res)):
            level_res = []
            matrix_res = ""
            for j in range(n):
                row_res = ""
                for k in range(n):
                    if res[i][j][k] == ".":
                        row_res += "."
                    else:
                        row_res += "Q"
                level_res.append(row_res)

            final_res.append(level_res)

        return final_res

    def helper(self, matrix_fill, row, n, res):

        if row > n:
            return

        if row == n:
            res.append(copy.deepcopy(matrix_fill))
            return

        for i in range(row, n):

            for j in range(n):

                if self.is_valid(matrix_fill, i, j, n):

                    matrix_fill[i][j] = "Q"

                    self.helper(matrix_fill, i + 1, n, res)

                    matrix_fill[i][j] = "."
            return

    def is_valid(self, matrix_fill, i, j, n):

        if i not in range(0, n) or j not in range(0, n):
            return False
        r, c = i, j

        while r >= 0:
            if matrix_fill[r][c] == "Q":
                return False
            r -= 1

        r, c = i, j

        while r >= 0 and c >= 0:
            if matrix_fill[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        r, c = i, j

        while r >= 0 and c < n:
            if matrix_fill[r][c] == "Q":
                return False
            r -= 1
            c += 1

        return True
