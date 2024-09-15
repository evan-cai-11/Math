from collections import deque
from typing import List

class Solution:
    def isNeighbor(self, s: str, r: str) -> bool:
        
        count = 0
        for i in range(len(s)):
            if s[i] != r[i]:
                count += 1

        return count == 1

    def buildGraph(self, wordList: List[str]):
        graph = {}
        for s in wordList:
            graph[s] = []
            for n in wordList:
                if self.isNeighbor(s, n):
                    graph[s].append(n)
        
        return graph

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = self.buildGraph(wordList)
        
        #find starting point
        visited = set()

        queue = deque()

        for s in wordList:
            if self.isNeighbor(beginWord, s):
                queue.append((s, 2))

        distance = 0
        while queue:
            s, dist = queue.popleft()

            if s in visited:
                continue

            if s == endWord:
                distance = dist
                break
            else:
                visited.add(s)
                for n in graph[s]:
                    queue.append((n, dist + 1))

        return distance

sol = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(sol.ladderLength(beginWord, endWord, wordList))

