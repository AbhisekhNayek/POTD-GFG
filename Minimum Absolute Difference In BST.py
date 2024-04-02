class Solution:
    def absolute_diff(self, root):
        # Helper function to perform inorder traversal and update minimum difference
        def inorder(node, prev, min_diff):
            if not node:
                return min_diff, prev
            min_diff, prev = inorder(node.left, prev, min_diff)
            if prev is not None:
                min_diff = min(min_diff, abs(node.data - prev))
            prev = node.data
            min_diff, prev = inorder(node.right, prev, min_diff)
            return min_diff, prev
        
        # Start inorder traversal with initial min_diff set to positive infinity and prev set to None
        min_diff, _ = inorder(root, None, float('inf'))
        
        return min_diff
