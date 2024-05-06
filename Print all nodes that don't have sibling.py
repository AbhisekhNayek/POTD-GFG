from typing import List


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def noSibling(root: Node) -> List[int]:
    
    if root is None:
        return [-1]
    
    alone = []
    traverse(root, alone)

    return sorted(alone) if len(alone) > 0 else [-1]

def traverse(root: Node, alone: List[int]):

    if root is None:
        return None
    
    left = traverse(root.left, alone)
    right = traverse(root.right, alone)

    if left is None and right is not None:
        alone.append(right.data)

    if right is None and left is not None:
        alone.append(left.data)
    
    return root
