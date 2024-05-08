class Solution:
    
    def __init__(self):
        self.all_paths = []
    
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        def get_paths(node, path):
            if node.left:
                get_paths(node.left, path + [node.data])
            if node.right:
                get_paths(node.right, path + [node.data])
            
            if not node.left and not node.right:
                self.all_paths.append(path + [node.data])
        
        if not root:
            return []
        
        path = []
        get_paths(root, path)
        return self.all_paths
