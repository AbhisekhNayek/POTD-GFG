class Solution:
    def kthCommonAncestor(self, root, k, x, y):
        # Helper function to find lowest common ancestor
        def findLCA(node, x, y):
            if not node:
                return None

            # If both x and y are smaller than current node, LCA lies in left subtree
            if x < node.data and y < node.data:
                return findLCA(node.left, x, y)
            
            # If both x and y are greater than current node, LCA lies in right subtree
            elif x > node.data and y > node.data:
                return findLCA(node.right, x, y)
            
            # If one is smaller and the other is greater than current node, LCA is the current node
            else:
                return node

        # Find lowest common ancestor
        lca = findLCA(root, x, y)

        # If LCA exists, find the kth ancestor
        if lca:
            ancestors = []
            self.findAncestors(root, lca, ancestors)
            return ancestors[-k] if len(ancestors) >= k else -1
        else:
            return -1

    # Helper function to find ancestors of a node
    def findAncestors(self, root, node, ancestors):
        if not root:
            return False

        if root.data == node.data:
            return True

        if (self.findAncestors(root.left, node, ancestors) or
                self.findAncestors(root.right, node, ancestors)):
            ancestors.append(root.data)
            return True

        return False
