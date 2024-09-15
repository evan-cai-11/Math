from typing import List

class Solution:
    def resetVisited(visited):
        for i in range(0, visited.length):
            for j in range(0, visited[0].length):
                visited = False

    def findIsland(self, grid: List[List[int]], visited: List[List[bool]], x: int, y: int):
        visited[y, x] = True

        surroundings = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for pos in surroundings:
            next_x += pos[0]
            next_y += pos[1]

            if (next_x >= 0 and next_x < len(grid[0]) 
                and next_y >= 0 and next_y < len(grid) 
                and visited[next_y, next_x] is False
                and grid[next_y, next_x] is True):
                self.findIsland(self, grid, visited, next_x, next_y)


    def minDays(self, grid: List[List[int]]) -> int:

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        total_island = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (visited[y, x] is False and grid[y, x] is True):
                    self.findIsland(self, grid, visited, x, y)
                    total_island += 1

        if total_island == 1:
            ## need to come up with algorithm
            return 1
        else:
            return 0

                