from typing import List

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        def dfs(start: int, edges: List[int], visited: List[int]) -> int:
            if edges[start] in visited:
                return 1
            else:
                visited.append(start)
                return 1 + dfs(edges[start], edges, visited)
            
        result = []
        for i in range(len(edges)):
            visited = []
            result.append(dfs(i, edges, visited))

        return result

sol = Solution()
edges = [1,2,0,0]
print(sol.countVisitedNodes(edges))
            
