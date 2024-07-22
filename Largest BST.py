#User function Template for python3
class Solution:
    def largestBst(self, root):
        def helper(node):
            # Base case: If the node is None, return size=0, min=inf, max=-inf, and is_bst=True
            if not node:
                return (0, float('inf'), float('-inf'), True)
            
            # Recursively get the properties of left and right subtrees
            l_size, l_min, l_max, l_is_bst = helper(node.left)
            r_size, r_min, r_max, r_is_bst = helper(node.right)
            
            # Check if the current node is the root of a BST
            if l_is_bst and r_is_bst and l_max < node.data < r_min:
                size = 1 + l_size + r_size
                min_val = min(l_min, node.data)
                max_val = max(r_max, node.data)
                return (size, min_val, max_val, True)
            else:
                return (max(l_size, r_size), 0, 0, False)
        
        size, _, _, _ = helper(root)
        return size



#{ 
 # Driver Code Starts
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size += 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()
        size -= 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)
            size += 1

        # Move to the next element
        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
            size += 1

        # Move to the next element
        i += 1

    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        result = ob.largestBst(root)
        print(result)

# } Driver Code Ends
