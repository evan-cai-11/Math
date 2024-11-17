from typing import List
from collections import deque

class Solution:

    def surround(self, row: int, col: int, board: List[List[str]]):
        queue = deque([(row, col)])
        neighbors = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        visited = set()

        touchBorder = False

        while queue:
            cur = queue.popleft()
            visited.add(cur)

            print("visited: ", visited)

            if cur[0] == 0 or cur[1] == 0 or cur[0] == len(board) - 1 or cur[1] == len(board[0]) - 1:
                touchBorder = True

            for offset_y, offset_x in neighbors:
                n_row = cur[0] + offset_y
                n_col = cur[1] + offset_x

                if n_row >= 0 and n_row < len(board) and n_col >= 0 and n_col < len(board[0]) and board[n_row][n_col] == "O" and (n_row, n_col) not in visited:
                    queue.append((n_row, n_col))

            
            print("queue:", queue)
        
        if not touchBorder:
            for r, c in visited:
                board[r][c] = "X"


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if (len(board) == 0 or len(board[0]) == 0):
            return

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    print(f"check at {row}, {col}")
                    self.surround(row, col, board)

sol = Solution()

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(board)

print(board)
        