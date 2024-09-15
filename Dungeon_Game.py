from typing import List

class Solution:

    def __init__(self, row, col):
        self.min_map: List[List[int]] = [[0 for _ in range(col)] for _ in range(row)]

    def dfs(self, map: List[List[int]], x: int, y: int) -> int:

        min_health = 0
        if y == len(map) - 1 and x == len(map[0]) - 1:
            min_health = -min(0, map[y][x]) + 1
        elif x == len(map[0]) - 1:
            min_health = max(1, -map[y][x] + self.dfs(map, x, y + 1)) 
        elif y == len(map) - 1:
            min_health = max(1, -map[y][x] + self.dfs(map, x + 1, y))
        else:
            down_health = self.dfs(map, x, y + 1)
            right_health = self.dfs(map, x + 1, y)

            min_health = max(1, -map[y][x] + min(down_health, right_health))

        print(f'x: {x}, y:{y}, cur: {map[y][x]}, min_health: {min_health}')
        self.min_map[y][x] = min_health
        return min_health

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        return self.dfs(dungeon, 0, 0)
    

dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
sol = Solution(len(dungeon), len(dungeon[0]))
print(sol.calculateMinimumHP(dungeon))
print(sol.min_map)
