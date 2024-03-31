class Solution:
    def findMaxForN(self, root, n):
        res=0
        def helper(root):
            nonlocal res
            if(root is None):
                return
            helper(root.left)
            if(root.key<=n):
                res=max(res,root.key)
            helper(root.right)
        helper(root)
        return res if res!=0 else -1
