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
                if len(queue) > 0 or cur.left or cur.right:

                    #print(f"push child of {cur.val}, queue size {len(queue)}, left {cur.left}, right: {cur.right}")
                    queue.append(cur.left)
                    queue.append(cur.right)
            else:
                data.append(None)

                # Trim trailing None values
        while data and data[-1] is None:
            data.pop()

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
root = []
ans = deser.deserialize(root)
print(ser.serialize(ans))