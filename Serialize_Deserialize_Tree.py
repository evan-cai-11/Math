from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        queue = deque([root])
        data = []

        while queue:
            cur = queue.popleft()
            if cur:
                data.append(cur.val)

                queue.append(cur.left)
                queue.append(cur.right)
            else:
                data.append(None)

        return data    
        

    def deserialize(self, data):
        if data is None or len(data) == 0:
            return None

        queue = deque()

        root = TreeNode(data[0])
        queue.append(root)

        i = 1
        while i < len(data):
            left = TreeNode(data[i]) if data[i] else None
            right = TreeNode(data[i + 1]) if i + 1 < len(data) and data[i + 1] else None

            parent = queue.popleft()

            if parent:
                parent.left = left
                queue.append(left)
                parent.right = right
                queue.append(right)

            i  += 2
            
        return root
        

#Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = [1,2,3,None,None,4, None, None, None]
ans = deser.deserialize(root)
print(ser.serialize(ans))