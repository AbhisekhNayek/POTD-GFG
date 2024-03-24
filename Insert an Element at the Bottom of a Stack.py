class Solution:
    def insertAtBottom(self, st, x):
        # code here
        modified_stack = [x]
        modified_stack.extend(st)
        return modified_stack
