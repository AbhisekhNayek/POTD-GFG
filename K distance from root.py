class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def KDistance(self,root,k):
        '''
        :param root: root of given tree.
        :param k: distance k from root
        :return: list of all nodes that are at distance k from root.
        '''
        # code here
        def solve(root, index, k, ans):
            if root == None:
                return
            if index == k:
                ans.append(root.data)
            solve(root.left, index + 1, k, ans)
            solve(root.right, index + 1, k, ans)
        ans = []
        solve(root, 0, k, ans)
        return ans
