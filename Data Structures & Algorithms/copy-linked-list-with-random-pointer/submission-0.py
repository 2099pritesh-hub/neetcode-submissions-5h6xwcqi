"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        def Lcopy(node):
            if not node:
                return
            copy = Node(node.val)
            oldToNew[node] = copy
            copy.next = Lcopy(node.next)
            if node.random:
                copy.random = oldToNew[node.random]
            return copy
        
        return Lcopy(head)
