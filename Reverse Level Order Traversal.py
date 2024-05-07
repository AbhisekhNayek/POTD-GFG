from collections import deque
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
    # code here
    ans = deque()
    q = deque([root])
    while q:
        c = q.popleft()
        ans.appendleft(c.data)
        if c.right:
            q.append(c.right)
        if c.left:
            q.append(c.left)
    return ans
