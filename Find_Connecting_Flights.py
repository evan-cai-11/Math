from typing import List

class Solution:

    def dfs(self, start: str, end: str, graph: dict[str, str], path: List[str]) -> bool:
        print(f"dfs: {start}, {end}")
        
        if start == end:
            path.append(start)
            return True
        
        if start not in graph:
            return False
        else:
            if self.dfs(graph[start], end, graph, path):
                path.append(start)
                return True
            else:
                return False

    def findFlightTickets(self, start: str, end: str, flights: List[List[str]]) -> List[str]:
        graph = {}
        
        for f in flights:
            graph[f[0]] = f[1]

        print(graph)
        
        path = []
        
        self.dfs(start, end, graph, path)

        path.reverse()

        return path
    
flights = [
    ['Chennai', 'Bangalore'],
    ['Bombay', 'Delhi'],
    ['Goa', 'Chennai'],
    ['Delhi', 'Goa'],
    ['Bangalore', 'Beijing']
]

sol = Solution()
print(sol.findFlightTickets('Bombay', 'Beijing', flights))              
