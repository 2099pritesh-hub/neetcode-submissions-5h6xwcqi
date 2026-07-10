# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if key == 0:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minNode = self.findMin(root.left)
                root.val = minNode.val
                root.left = self.deleteNode(root.left, minNode.val)
        return root
    
    def findMin(self, node):
        cur = node
        while cur.right:
            cur = cur.right
        return cur