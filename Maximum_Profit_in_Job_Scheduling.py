from typing import List

class Node:
    def __init__(self, index: int, startTime: int, endTime: int, profit: int):
        self.index = index
        self.startTime = startTime
        self.endTime = endTime
        self.profit = profit

class Solution:

    def buildGraph(self, startTime: List[int], endTime: List[int], profit: List[int]) -> dict[int, List[int]]:
        graph = {}
        
        for i in range(len(startTime)):
            graph[i] = []
            
            for j in range(len(startTime)):
                if i != j and endTime[i] <= startTime[j]:
                    graph[i].append(j)

        return graph

    def printList(self, list: List[Node]):
        for n in list:
            print(f"Index: {n.index}, start: {n.startTime}, end: {n.endTime}, profit: {n.profit}")
    
    def dfs(self, start: int, graph: dict[int, List[int]], startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        if len(graph[start]) == 0:
            return profit[start]
        
        max_profit = 0
        for i in graph[start]:
            max_profit = max(max_profit, self.dfs(i, graph, startTime, endTime, profit))

        return max_profit + profit[start]


    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        graph = self.buildGraph(startTime, endTime, profit)
        max_profit = 0

        for i in range(len(startTime)):
            max_profit = max(max_profit, self.dfs(i, graph, startTime, endTime, profit))

        return max_profit

sol = Solution()
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

print(sol.jobScheduling(startTime, endTime, profit))