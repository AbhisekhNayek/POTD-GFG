class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Solution:
    def sumOfLongRootToLeafPath(self, root):
        # Helper function to perform DFS and find the longest path sum
        def dfs(node, level, current_sum, max_path_length, max_path_sum):
            if node is None:
                if max_path_length < level:
                    max_path_length = level
                    max_path_sum = current_sum
                elif max_path_length == level:
                    max_path_sum = max(max_path_sum, current_sum)
                return max_path_length, max_path_sum

            # Recursive calls for left and right subtrees
            left_path_length, left_path_sum = dfs(node.left, level + 1, current_sum + node.data, max_path_length, max_path_sum)
            right_path_length, right_path_sum = dfs(node.right, level + 1, current_sum + node.data, max_path_length, max_path_sum)

            # Compare and return the maximum path length and sum
            if left_path_length > right_path_length:
                return left_path_length, left_path_sum
            elif right_path_length > left_path_length:
                return right_path_length, right_path_sum
            else:
                return left_path_length, max(left_path_sum, right_path_sum)

        max_path_length, max_path_sum = dfs(root, 0, 0, 0, 0)
        return max_path_sum  # Return the maximum sum of nodes on the longest path
