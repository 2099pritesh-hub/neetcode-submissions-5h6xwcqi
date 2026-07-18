"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def clone(node, oldTonew):
            if not node:
                return None
            if node in oldTonew:
                return oldTonew[node]

            copy = Node(node.val)
            oldTonew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor, oldTonew))
            return copy
        
        return clone(node, {})