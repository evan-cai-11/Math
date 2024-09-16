from typing import List

class Solution:
    def findPrimes(self, n: int) -> List[int]:
        primes = [2]
        for i in range(3, n+1):
            isPrime = True

            for j in range(len(primes)):
                if i % primes[j] != 0:
                    j += 1
                else:
                    isPrime = False
                    break
            
            if isPrime:
                primes.append(i)

        return primes

    def buildGraph(self, edges: List[List[int]]) -> dict[int, List[int]]:
        graph = {}

        for a, b in edges:
            if a not in graph:
                graph[a] = [b]
            else:
                graph[a].append(b)

            if b not in graph:
                graph[b] = [a]
            else:
                graph[b].append[a]
        
        return graph
    
    def isValidPath(self, start: int, end: int, parent: int, foundPrime: bool, graph, primes) -> bool:
        print(f"Processing start {start}, end {end}, foundPrime: {foundPrime}")
        
        if start in primes and foundPrime:
            return False
        
        if start in primes:
            foundPrime = True

        if start == end:
            return foundPrime

        for next in graph[start]:
            if next != parent:
                result = self.isValidPath(next, end, start, foundPrime, graph, primes)
                if result:
                    return True

        return False

    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        primes = self.findPrimes(n)
        graph = self.buildGraph(edges)

        count = 0
  
        for i in range(1, n):
            for j in range(i + 1, n):
                if self.isValidPath(i, j, -1, False, graph, primes):
                    print(f"Found valid path between: {i}, {j}")
                    count += 1

        return count

sol = Solution()
n = 5
edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
primes = sol.findPrimes(n)
graph = sol.buildGraph(edges)
print(graph)
print(primes)
#print(sol.isValidPath(3, 4, -1, False, graph, primes))
print(sol.countPaths(5, edges))