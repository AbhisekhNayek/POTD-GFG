from collections import deque

class Solution:
    # Function to return the level order traversal of a tree.
    def levelOrder(self, root):
        if not root:
            return []
        
        q = deque([root])
        res = []
        
        while q:
            node = q.popleft()
            res.append(node.data)  
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
        return res
