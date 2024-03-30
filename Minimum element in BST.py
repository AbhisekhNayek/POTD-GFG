class Solution:
    def minValue(self, root):
        if root.left:return self.minValue(root.left)
        return root.data
