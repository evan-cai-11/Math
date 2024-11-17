from typing import List 
from collections import deque

class Solution:

    def visit(self, x: int, y: int, visited: List[List[int]], grid: List[List[int]]) -> int:

        print(f"Visiting {y}, {x}")
        
        if grid[y][x] == 1:
            return -1
        elif x == len(grid[0]) - 1 and y == len(grid) - 1:
            print("Found destination")
            visited[y][x] = 1
            return 1
        else:
            min_path = self.MAX_PATH_LENGTH
            visited[y][x] = self.MAX_PATH_LENGTH
            for i in range(max(0, y-1), min(y+2, len(grid))):
                for j in range(max(0, x-1), min(x+2, len(grid[0]))):
                    if (i != y or j != x) and grid[i][j] == 0:
                        print(f"Explore {i}, {j}")
                        print(visited)
                        if (visited[i][j] != 0):
                            path_len = visited[i][j]
                        else:
                            path_len = self.visit(j, i, visited, grid)

                        if path_len != -1 and path_len < min_path:
                            min_path = path_len

            if min_path == self.MAX_PATH_LENGTH:
                visited[y][x] = -1
                return -1
            else:
                visited[y][x] = min_path + 1
                return min_path + 1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return -1
        
        n = len(grid)
        
        if grid[0][0] != 0 or grid[n-1][n-1]:
            return -1

        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        visited = set([(0, 0)])
        queue = deque([(0, 0, 1)])

        while queue:
            row, col, distance = queue.popleft()
            print(f"Dequeue {row}, {col}")
            if row == n - 1 and col == n - 1:
                return distance

            for offset_row, offset_col in neighbors:
                cur_row, cur_col = row + offset_row, col + offset_col

                if cur_row >= 0 and cur_row < n and cur_col >=0 and cur_col < n and grid[cur_row][cur_col] == 0 and (cur_row, cur_col) not in visited:
                    visited.add((cur_row, cur_col))
                    queue.append((cur_row, cur_col, distance + 1))
                    print (f"Enqueue: {cur_row}, {cur_col}, {distance + 1}")

        print(visited)

        return -1

        

sol = Solution()
grid = [[0,0,0],[1,0,0],[1,1,0]]
print(sol.shortestPathBinaryMatrix(grid))