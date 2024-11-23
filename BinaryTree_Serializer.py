class Deserializer:
    def deserialize(self, data: str) -> TreeNode:
        """
        Deserializes a binary tree from its preorder traversal string.
        Format: Values are comma-separated, null nodes are represented as 'null'
        Example: "1,2,null,null,3,4,null,null,5,null,null"
        """
        if not data:
            return None
            
        # Split the string into a list of values
        values = data.split(',')
        self.index = 0
        
        def dfs() -> TreeNode:
            # Base case: if we've processed all nodes or current is null
            if self.index >= len(values) or values[self.index] == 'null':
                self.index += 1
                return None
            
            # Create current node
            node = TreeNode(int(values[self.index]))
            self.index += 1
            
            # Recursively construct left and right subtrees
            node.left = dfs()
            node.right = dfs()
            
            return node
            
        return dfs()