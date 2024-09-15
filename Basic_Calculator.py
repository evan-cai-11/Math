from collections import deque

class TreeNode:
    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findClosingParan(self, s: str, start: int) -> int:
        open_paran = 0
        for i in range(start, len(s)):
            if s[i] == '(':
                open_paran += 1
            
            if s[i] == ')':
                if open_paran == 0:
                    return i
                else:
                    open_paran -= 1


    def buildOperationTree(self, s: str) -> TreeNode:
        print('build tree for: ', s)

        if len(s) == 0:
            return None
        
        root = None
        
        left_paran = s.find('(')
        right_paran = self.findClosingParan(s, left_paran + 1)

        if (left_paran == 0):
            if (right_paran == len(s) - 1):
                root = self.buildOperationTree(s[left_paran + 1: right_paran])
            else:
                root = TreeNode(s[right_paran+1])
                root.left = self.buildOperationTree(s[left_paran + 1: right_paran])
                root.right = self.buildOperationTree(s[right_paran+2:])
        elif (left_paran > 0):
            root = TreeNode(s[left_paran-1])
            root.left = self.buildOperationTree(s[0:left_paran - 1])
            root.right = self.buildOperationTree(s[left_paran: ])
        else:
            op = s.find('+')
            if op < 0:
                op = s.find('-')

            if op >= 0:
                root = TreeNode(s[op])
                root.left = self.buildOperationTree(s[0:op])
                root.right = self.buildOperationTree(s[op+1:])
            else:
                root = TreeNode(s)

        return root

    def evalTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        left = self.evalTree(root.left)
        right = self.evalTree(root.right)


        if (root.val == '+'):
            print(f'Evaluate expression: {left} {root.val} {right}')

            return left + right
        elif (root.val == '-'):
            print(f'Evaluate expression: {left} {root.val} {right}')

            return left - right
        else:
            return int(root.val)

    def calculate(self, s: str) -> int:
        s.replace(' ', '')
        root = self.buildOperationTree(s)
        return self.evalTree(root)


sol = Solution()
s = "(1+(4+5+2)-3)+(6+8)"
print(sol.calculate(s))
