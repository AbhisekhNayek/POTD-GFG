class Solution:
    def zigZagTraversal(self, root):
        queue = [root]
        result = []
        flag = 1
        while queue:
            temp = []
            current_level = []
            for node in queue:
                current_level.append(node.data)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
            if flag:
                result.extend(current_level)
            else:
                result.extend(current_level[::-1])
            flag = 1 - flag
        return result
