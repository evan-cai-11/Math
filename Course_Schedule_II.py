from typing import List

class Solution:

    def createGraph(self, prerequisites: List[List[int]]) -> dict[int, set[int]]:
        graph = {}

        for c, p in prerequisites:
            if c in graph:
                graph[c].add(p)
            else:
                graph[c] = set([p])

        return graph

    def dfs(self, c: int, graph: dict[int, set[int]], visited: set[int], path: List[int], results: List[int]) -> bool:
        
        # in topological sort, if any circular dependency is detected 
        if c in path:
            return False
        
        # in topological sort, if a node is visited, that means that path forward is explored
        # The previous result might be success or failure
        # If success: means all the prereq is done, then this exploration should return success
        # If fail: means there's a circular dependency, it's impossible to have complete sort
        # Therefore even this is set to True, it doesn't impact overall result
        if c in visited:
            return True
        
        visited.add(c)
        path.append(c)

        print("visited: ", visited)
        print("path: ", path)

        if c in graph:
            for n in graph[c]:
                if not self.dfs(n, graph, visited, path, results):
                    return False
        
        path.remove(c)
        results.append(c)
        print("results: ", results)
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.createGraph(prerequisites)

        print("Graph: ", graph)

        visited = set()
        path = []
        results = []

        for c in range(numCourses):
            if not self.dfs(c, graph, visited, path, results):
                return []
            
        return results
    
sol = Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print("Final: ", sol.canFinish(numCourses, prerequisites))
                
