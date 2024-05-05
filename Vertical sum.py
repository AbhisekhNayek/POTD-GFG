from collections import deque


class Solution:
    #Complete the function below
    def verticalSum(self, root):
        #:param root: root of the given tree.
        
        if not root:
            
            return None
            
        dq = deque()
        
        dq.append((root,0))
        
        dc = dict()
        
        while dq:
            
            node, level = dq.popleft()
            
            dc[level] = dc.get(level, 0) + node.data
            
            if node.left:
                
                dq.append((node.left, level-1))
                
            if node.right:
                
                dq.append((node.right, level+1))
                
                
        return [dc[l] for l in sorted(dc.keys())]
        
