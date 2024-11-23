from typing import List

class Solution:

    def dfs(self, c: str, graph: dict[str, set[str]], visited: set[str], path: List[str]) -> bool:
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
        
        if c in graph:
            for n in graph[c]:
                if not self.dfs(n, graph, visited, path):
                    return False

        # finished exploreing all the child and this node, pop it out of the path            
        path.remove(c)
        return True
    
    def printPath(self, c: str, graph: dict[str, set[str]], visited: set[str], result: List[str]):
        if c in visited:
            return
        else:
            visited.add(c)
        
        if len(graph[c]) > 0:
            for n in graph[c]:
                self.printPath(n, graph, visited, result)

        result.append(c)


    def alienOrder(self, words: List[str]) -> str:
        graph = {}

        for i in range(0, len(words)):
            if i == 0:
                for c in words[i]:
                    if c not in graph:
                        graph[c] = set()
            else:
                prev = words[i - 1]
                for j in range(0, len(words[i])):
                    if j < len(prev) and prev[j] != words[i][j]:
                        if words[i][j] not in graph:
                            graph[words[i][j]] = set()

                        graph[words[i][j]].add(prev[j])

        visited = set()
        path = []

        for a in graph:
            if not self.dfs(a, graph, visited, path):
                return ""
            
        visited = set()
        result = []

        for a in graph:
            self.printPath(a, graph, visited, result)

        return ''.join(x for x in result)

words = ["wrt","wrf","er","ett","rftt"]
sol = Solution()
print(sol.alienOrder(words))