from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    @staticmethod
    def constructTreeBFS(input: List[int]) -> TreeNode:
        if len(input) == 0:
            return None
        
        root = TreeNode(input[0])

        queue = deque([root])

        idx = 1

        while queue:
            parent = queue.popleft()
            if parent is None:
                continue
            
            if idx < len(input):
                parent.left = None if input[idx] is None else TreeNode(input[idx])
                parent.right = None if input[idx + 1] is None else TreeNode(input[idx + 1])
                queue.append(parent.left)
                queue.append(parent.right)
                idx += 2

        return root
    
    @staticmethod
    def printTreeBFS(root: TreeNode) -> List[int]:
        result = []

        if root is not None:
            queue = deque([root])

            while queue:
                parent = queue.popleft()

                if parent is not None:
                    result.append(parent.val)
                    queue.append(parent.left)
                    queue.append(parent.right)
                else:
                    result.append(None)

        return result



class Solution:
    def __init__(self):
        self.nodes = []

    def traverseTree(self, node: TreeNode, parent: TreeNode, depth: int):
        if node is None:
            return

        self.nodes.append((node, parent, depth))
        if node.left is not None:
            self.traverseTree(node.left, node, depth + 1)
        
        if node.right is not None:
            self.traverseTree(node.right, node, depth + 1)

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            self.traverseTree(root, None, 0)

            results = {}
            for i in range(0, len(self.nodes)):
                if self.nodes[i][0] not in results:
                    results[self.nodes[i][0]] = 0

                for j in range (i + 1, len(self.nodes)):
                    if self.nodes[j][0] not in results:
                        results[self.nodes[j][0]] = 0
                    
                    if self.nodes[i][2] == self.nodes[j][2] and self.nodes[i][1] != self.nodes[j][1]:
                        results[self.nodes[i][0]] += self.nodes[j][0].val
                        results[self.nodes[j][0]] += self.nodes[i][0].val

            for node in results:
                node.val = results[node]

        return root
    
input = [5,4,9,1,10,None,7]
root = BinaryTree.constructTreeBFS(input)

sol = Solution()
updatedTree = sol.replaceValueInTree(root)
print(BinaryTree.printTreeBFS(root))


