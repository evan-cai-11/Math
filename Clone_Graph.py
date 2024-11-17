from typing import List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:

    def createGraph(self, adjList: List[List[int]]) -> {int, Node} :
        nodes = {}

        for dest, src in adjList:
            destNode = None
            if dest not in nodes:
                destNode = Node(dest)
                nodes[destNode.val] = destNode
            else:
                destNode = nodes[dest]

            srcNode = None
            if src not in nodes:
                srcNode = Node(src)
                nodes[srcNode.val] = srcNode
            else:
                srcNode = nodes[src]

            destNode.neighbors.append(srcNode)
            srcNode.neighbors.append(destNode)

        return nodes

    def cloneGraph(self, node: Optional[Node]):
        if node is None:
            return None

        queue = deque([node])

        nodes = {node.val:Node(node.val)}

        while queue:
            cur: Node = queue.popleft()

            curClone = None
            if cur.val not in nodes:
                curClone = Node(cur.val)
            else:
                curClone = nodes[cur.val]

            for neighbor in cur.neighbors:
                neighborClone = None
                if neighbor.val not in nodes:
                    queue.append(neighbor)
                    neighborClone = Node(neighbor.val)
                    nodes[neighbor.val] = neighborClone
                else:
                    neighborClone = nodes[neighbor.val]
                
                curClone.neighbors.append(neighborClone)

        return nodes[node.val]
    
    def printGraph(self, graph: {int, Node}):
        for _, node in graph.items():
            print(f"{node.val} ({len(node.neighbors)}) ->" + ', '.join(map(lambda x: str(x.val), node.neighbors)))
    

sol = Solution()
graph = sol.createGraph([[1, 2],[2,3],[3,4],[1,4]])
sol.printGraph(graph)
cloneNode, cloneGraph = sol.cloneGraph(graph[3])
sol.printGraph(cloneGraph)

