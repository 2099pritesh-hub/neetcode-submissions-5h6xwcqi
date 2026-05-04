# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        positionInInorder = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : positionInInorder + 1], inorder[: positionInInorder])
        root.right = self.buildTree(preorder[positionInInorder + 1 :], inorder[positionInInorder + 1 :])
        return root