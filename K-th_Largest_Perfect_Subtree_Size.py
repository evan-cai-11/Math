# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.results = []

    def isPerfectTree(self, n: TreeNode)->int: 
        if n.left == None and n.right == None:
            self.results.append(1)
            return 1
        elif n.left == None or n.right == None:
            return -1
        else:
            left = self.isPerfectTree(n.left)
            right = self.isPerfectTree(n.right)

            if left > 0 and right > 0 and left == right:
                self.results.append(left + right + 1)
                return left + right + 1
            else:
                return -1


    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        else:
            self.isPerfectTree(root)
            
            if k > len(self.results):
                return -1
            else:
                
                self.results.sort(reverse=True)
                print(self.results)
                return self.results[k-1]