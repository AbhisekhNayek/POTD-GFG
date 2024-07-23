#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BSTIterator:
    def __init__(self, root):
        self.st = []
        self.push_all(root)
    
    def hasnext(self):
        return len(self.st) > 0
    
    def getItem(self):
        temp = self.st.pop()
        if temp.right:
            self.push_all(temp.right)
        return temp.data
    
    def push_all(self, root):
        while root:
            self.st.append(root)
            root = root.left

class Solution:
    def merge(self, root1, root2):
        ans = []
        
        bst1 = BSTIterator(root1)
        bst2 = BSTIterator(root2)
        
        if bst1.hasnext():
            a = bst1.getItem()
        else:
            a = None
        
        if bst2.hasnext():
            b = bst2.getItem()
        else:
            b = None
        
        while a is not None and b is not None:
            if a <= b:
                ans.append(a)
                if bst1.hasnext():
                    a = bst1.getItem()
                else:
                    a = None
            else:
                ans.append(b)
                if bst2.hasnext():
                    b = bst2.getItem()
                else:
                    b = None
        
        while a is not None:
            ans.append(a)
            if bst1.hasnext():
                a = bst1.getItem()
            else:
                a = None
        
        while b is not None:
            ans.append(b)
            if bst2.hasnext():
                b = bst2.getItem()
            else:
                b = None
        
        return ans

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == 'N':
        return None
    
    # Creating list of strings from input string after splitting by space
    ip = s.split()
    
    # Create the root of the tree
    root = Node(int(ip[0]))
    
    # Push the root to the queue
    queue = [root]
    
    # Starting from the second element
    i = 1
    while queue and i < len(ip):
        # Get and remove the front of the queue
        currNode = queue.pop(0)
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.left)
        
        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            
            # Push it to the queue
            queue.append(currNode.right)
        i += 1
    
    return root



def main():
    t = int(input())
    for _ in range(t):
        s = input()
        root1 = buildTree(s)
        s = input()
        root2 = buildTree(s)
        obj = Solution()
        vec = obj.merge(root1, root2)
        print(" ".join(map(str, vec)))

if __name__ == "__main__":
    main()

# } Driver Code Ends
